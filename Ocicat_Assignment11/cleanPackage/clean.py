import csv

class CSVCleaner:
    def __init__(self, data):
        self.data = data

    def format_gross_price(self):
        """
        Make sure the Gross Price column has exactly 2 decimal places.
        Assumes Gross Price is in a column labeled 'Gross Price'.
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
