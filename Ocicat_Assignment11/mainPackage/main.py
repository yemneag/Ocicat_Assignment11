# main.py
from anomalyPackage import anomaly
from cleanPackage.clean import *
from exportPackage.export import CSVExporter
from utilPackage.util import *
from anomalyPackage.anomaly import *
from apiPackage.api import ZipCodeAPI
from exportPackage.export import CSVExporter

# Extra Credit Documentation
# Side ID's are right and left justified , and they randomly chnage between letters and numbers 
# The Addresses being in one column isnt very effecient for clean data 
# The addresses are formatted differently which makes it hard to parse 
# Fuel quantity are all different decimal points 


if __name__ == "__main__":
    def main():
        data = CSVinput.read_CSV_file()
        cleaner = CSVCleaner(data)
        cleaner.format_gross_price()
        cleaner.remove_duplicates()
        anomaly_detector = AnomalyDetector(cleaner.get_clean_data())
        anomaly_detector.filter_pepsi_purchases()
        anomaly_detector.save_anomalies()
        almost_clean = anomaly_detector.get_clean_data()
        updater = ZipCodeAPI(almost_clean)
        updater.update_missing_zipcodes(almost_clean)
       
        export = CSVExporter
        CSVExporter.export_cleaned_data(updater.get_clean_data())
        
    main()
   


