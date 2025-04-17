# export.py 

import csv
import os

class CSVExporter:
    @staticmethod
    def export_cleaned_data(data, filepath="./Data/cleanedData.csv"):
        """
        Writes cleaned data to cleanedData.csv in the Data folder.
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
