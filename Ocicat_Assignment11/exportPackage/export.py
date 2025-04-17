# export.py
# File Name : export.py
# Student Name: Abel Yemaneab, Hailey Manuel
# email: yemaneag@mail.uc.edu, manuehv@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section: IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This Assignment teaches us how to clean data, parse throught the results, and input into a seperate csv file
# Brief Description of what this module does. This module exports the final cleaned data to a CSV file.
# Citations: https://www.geeksforgeeks.org/writing-csv-files-in-python/
import csv
import os

class CSVExporter:
    @staticmethod
    def export_cleaned_data(data, filepath="./Data/cleanedData.csv"):
        """
        Writes the final cleaned data to cleanedData.csv in the Data folder.
        """
        if not data:
            print("No cleaned data available to export.")
            return

        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        print(f"Cleaned data successfully exported to {filepath}")
