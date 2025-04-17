# clean.py
# File Name : clean.py
# Student Name: Abel Yemaneab, Hailey Manuel
# email: yemaneag@mail.uc.edu, manuehv@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section: IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This Assignment teaches us how to clean data, parse throught the results, and input into a seperate csv file
# Brief Description of what this module does. This module takes the data from util.py and formats the data
# Citations: We used chatgpt
import csv

class CSVCleaner:
    def __init__(self, data):
        self.data = data

    def format_gross_price(self):
        """
        Formats gross price to only have two decimal places.
        """
        cleaned_data = []
        for row in self.data:
            try:
                row['Gross Price'] = "{:.2f}".format(float(row['Gross Price']))
                cleaned_data.append(row)
            except ValueError:
                print(f"Invalid Gross Price for row: {row}")
        self.data = cleaned_data

    def remove_duplicates(self):
        """
        Removes duplicate rows.
        """
        seen = set()
        unique_data = []
        for row in self.data:
            row_tuple = tuple(row.items())
            if row_tuple not in seen:
                seen.add(row_tuple)
                unique_data.append(row)
        self.data = unique_data

    def get_clean_data(self):
        return self.data

