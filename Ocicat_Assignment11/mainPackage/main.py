# main.py
from cleanPackage.clean import *
from utilPackage.util import *
from anomalyPackage.anomaly import *


if __name__ == "__main__":
    def main():
        data = CSVinput.read_CSV_file()
        cleaner = CSVCleaner(data)
        cleaner.format_gross_price()
        cleaner.remove_duplicates()
        anomaly_detector = AnomalyDetector(cleaner.get_clean_data())
        anomaly_detector.filter_pepsi_purchases()
        anomaly_detector.save_anomalies()
    
    main()