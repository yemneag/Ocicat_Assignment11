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
    @staticmethod
    def read_CSV_file():
        '''
        Reads fuelPurchaseData.csv into a list of dictionaries.
        The first row is used as keys.
        @return list: the list of dictionaries from the file.
        '''
        csv_data = []
        with open("./Data/fuelPurchaseData.csv", newline='') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                csv_data.append(row)
        return csv_data