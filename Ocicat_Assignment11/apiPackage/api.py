# api.py
# File Name : api.py
# Student Name: Abel Yemaneab, Hailey Manuel
# email: yemaneag@mail.uc.edu, manuehv@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section: IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This Assignment teaches us how to clean data, parse throught the results, and input into a seperate csv file
# Brief Description of what this module does. This module uses the api to fill in the missing zip code for cities 
# Citations: We used chatgpt

import requests

class ZipCodeAPI:
    """
    A class to interact with the ZipCodeBase API and update missing ZIP codes in data rows that include a 'Full Address' field.
    """

    def __init__(self,data):
        self.api_key = 'c11deba0-1b74-11f0-a1d7-bfeed43e07f4'  
        self.base_url = 'https://app.zipcodebase.com/api/v1/code/city'
        self.data = data
    def request_api_zipcode(self, city, state_name):
        """
        Get a list of ZIP codes for the given city and state.
        """
        params = {
            "apikey": self.api_key,
            "city": city,
            "state_name": state_name,
            "country": "us"
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            if "results" in data and isinstance(data["results"], list) and data["results"]:
                return data["results"]
            else:
                print(f" No ZIPs found for {city}, {state_name}")
                return None

        except requests.RequestException as e:
            print(f"API request failed for {city}, {state_name}: {e}")
            return None

    def extract_city_state(self, full_address):
        """
        Try to extract city and state from a full address string.
        Returns a (city, state) tuple.
        """
        if not full_address:
            return None, None

        
        parts = [p.strip() for p in full_address.split(',')]

        # Handle more complex or misformatted addresses
        if len(parts) == 3:
            # Case: "4232 Cougar Parkwy, Lynchburg, OH"
            city = parts[1]
            state = parts[2] if len(parts) > 2 else None
            return city, state
    
        elif len(parts) == 4:
            # Case: "43251 OH, Columbus, 3099 Daylight Street"
            city = parts[1]
            state = parts[0].strip().split()[1]  # Extract the state from the first part
            return city, state

        elif len(parts) == 5:
            # Case: "2428 Pennsylvania St, Zanesville, OH 43702"
            city = parts[1]
            state = parts[2]
            return city, state

        else:
            return None, None



    def update_missing_zipcodes(self, data):
        """
        Loops through ONLY the first 5 rows and updates missing ZIP codes
        by extracting city/state from 'Full Address'.
        Returns the updated dataset.
        """
        updated_data = []
        count = 0
        max_rows = 5

        for row in data:
            if count >= max_rows:
                updated_data.append(row)
                continue 

            if row.get("Zip", "").strip():  
                updated_data.append(row)
                continue

            full_address = row.get("Full Address", "").strip()
            city, state = self.extract_city_state(full_address)

            
            if state == "OH":
                state = "Ohio"

            if city and state:
                zip_list = self.request_api_zipcode(city, state)
                if zip_list:
                    row["Zip"] = zip_list[0]
                    print(f"Updated ZIP for {city}, {state}: {zip_list[0]}")
                else:
                    print(f" No ZIPs found for {city}, {state}")
                    row["Zip"] = ""
            else:
                print(f"Could not extract city/state from: {full_address}")
                row["Zip"] = ""

            updated_data.append(row)
            count += 1
        self.data = updated_data