# main.py
from cleanPackage.clean import *
from utilPackage.util import *

if __name__ == "__main__":
    def main():
        # Get data from CSVinput
        data = CSVinput.read_CSV_file()

        # Pass the data to the cleaner
        cleaner = CSVCleaner(data)
        cleaner.format_gross_price()
        cleaner.remove_duplicates()