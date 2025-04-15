# util.py
# File Name : util.py
# Student Name: Abel Yemaneab, Hailey Manuel
# email: yemaneag@mail.uc.edu, manuehv@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section: IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This Assignment teaches us how to clean data, parse throught the results, and input into a seperate csv file
# Brief Description of what this module does. This module reads the cvs file
# Citations: https://www.geeksforgeeks.org/convert-json-to-csv-in-python/, https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv


import csv

class CSVinput:
    def read_CSV_file():
        '''
        Read a particular CSV file into a list of lists.
        fuelPurchaseData.csv
        The first row is assumed to be a header and is skipped
        @return list: the list of lists that was created from the file
        '''
        csv_data = []
        # In a Visual Studio project, the default folder is the project folder. It is not the package containing the entry point. 
        with open("./data/fuelPurchaseData.csv", newline='') as f:
            reader = csv.reader(f, delimiter=',')
            header = next(reader)
        #   csv_data.append(header)        # We don't want the header row.
            for row in reader:
                csv_data.append(row)
    
        #print(csv_data)
        #print (type(csv_data))      # It's a list of lists!
        return csv_data