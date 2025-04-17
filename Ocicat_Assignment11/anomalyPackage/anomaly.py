# anomaly.py
# File Name : anomaly.py
# Student Name: Abel Yemaneab, Hailey Manuel
# email: yemaneag@mail.uc.edu, manuehv@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section: IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This Assignment teaches us how to clean data, parse throught the results, and input into a seperate csv file
# Brief Description of what this module does. This module filters out anomalies from the data.
# Citations:
import csv
import os

class AnomalyDetector:
    def __init__(self, data):

        self.data = data
        self.anomalies = []

    def filter_pepsi_purchases(self):
        """
        This def takes out all rows with pepsi in the Fuel Type column.
        It stores the removed rows in the anomalies list.
        """
        clean_data = []
        for row in self.data:
            fuel_type = row.get('Fuel Type', '').strip().lower()
            if 'pepsi' in fuel_type:
                self.anomalies.append(row)
            else:
                clean_data.append(row)
        self.data = clean_data

    def save_anomalies(self, filepath="./Data/dataAnomalies.csv"):
        """
        This def saves the anomalies to a CSV file.
        """
        if not self.anomalies:
            print("No anomalies found to save.")
            return

        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.anomalies[0].keys())
            writer.writeheader()
            writer.writerows(self.anomalies)

    def get_clean_data(self):
        """
        Returns the cleaned data (Pepsi rows removed).
        """
        return self.data

