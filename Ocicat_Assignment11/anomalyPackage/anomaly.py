import csv
import os

class AnomalyDetector:
    def __init__(self, data):
        """
        Initializes with a list of dictionaries (rows of data).
        """
        self.data = data
        self.anomalies = []

    def filter_pepsi_purchases(self):
        """
        Removes rows where the Fuel Type contains 'pepsi'.
        Saves these rows into the 'anomalies' list.
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
        Saves Pepsi rows to dataAnomalies.csv in the Data folder.
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

