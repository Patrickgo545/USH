import pandas as pd
import difflib
import re

def clean_with_regex(column, pattern, replace_with=""):
    return column.apply(lambda x: re.sub(pattern, replace_with, str(x)))
import re

def clean_column(column, pattern=r'[^\d\.]', dtype=float):
    return column.apply(lambda x: re.sub(pattern, '', str(x))).astype(dtype)


class ShippingData:
    def __init__(self):
        self.shipments_df = None
        self.monthly_gas_averages = None
        self.df = None
        self.outbound_df = None
        self.inbound_df = None
        self.COLUMN_MAPPING = {
            "outbound_columns": [
                "Outbound # of Pallets", "Outbound Total Weight (in lbs)", "Outbound Type of Truck",
                "Price Quoted for Outbound", "One Way Distance To/From Warehouse", "avg_gas_price",
                "Load In Date & Time"
            ], #, "isMajorCity"
            "inbound_columns": [
                "Return # of Pallets", "Return Total Weight", "Return Type of Truck",
                "Price Quoted for Return", "One Way Distance To/From Warehouse", "avg_gas_price",
                "Load Out Date & Time"
            ] #, "isMajorCity
        }

     
    def is_major_city(city):
        major_cities = ["new york", "nyc", "ny", "chicago", "san francisco", "san fran", "los angeles", "la"]
        closest_match = difflib.get_close_matches(city.lower(), major_cities)
        return closest_match and closest_match[0] == city.lower()

    @staticmethod
    def is_shipment_on_weekend(shipment_date):
        return shipment_date.weekday() in [5, 6]
     
    def load_csv(self, csv_path, dataset_type="shipments"):
        if dataset_type == "shipments":
            self.shipments_df = pd.read_csv(csv_path)
            self.shipments_df['Project Date'] = pd.to_datetime(self.shipments_df['Project Date'], format='%Y-%m-%d')
        elif dataset_type == "gas_averages":
            self.monthly_gas_averages = pd.read_csv(csv_path)

    def process_data(self):
        # Merge and process data
        self.shipments_df['month_year'] = self.shipments_df['Project Date'].dt.month.astype(str) + '/' + \
                                          self.shipments_df['Project Date'].dt.year.astype(str)
        self.shipments_df = pd.merge(self.shipments_df, self.monthly_gas_averages, how='left',
                                     left_on='month_year', right_on='Month')
        self.shipments_df.rename(columns={'U.S. All Grades All Formulations Retail Gasoline Prices Dollars per Gallon': 'avg_gas_price'}, inplace=True)
     #    self.shipments_df['isMajorCity'] = self.shipments_df['HP City'].apply(self.is_major_city)

    def create_dataframe(self):
        outbound_df = self.shipments_df[self.COLUMN_MAPPING['outbound_columns']]
        inbound_df = self.shipments_df[self.COLUMN_MAPPING['inbound_columns']]
        self.df = self._generate_combined_dataframe(outbound_df, inbound_df)
        
        # Clean columns
        self.df['weight'] = clean_with_regex(self.df['weight'], r"[^\d.]", "").astype(float)
        self.df['distance'] = clean_with_regex(self.df['distance'], r"[^\d.]", "").astype(float)
        self.df['quote'] = clean_with_regex(self.df['quote'], r"[^\d.]", "").astype(float)
        self.df['pallets'] = clean_with_regex(self.df['pallets'], r"[^\d.]", "").astype(float)

    def _generate_combined_dataframe(self, outbound_df, inbound_df):
        df = pd.DataFrame({
            'pallets': pd.concat([outbound_df['Outbound # of Pallets'], inbound_df['Return # of Pallets']], ignore_index=True),
            'weight': pd.concat([outbound_df['Outbound Total Weight (in lbs)'], inbound_df['Return Total Weight']], ignore_index=True),
            'distance': pd.concat([outbound_df['One Way Distance To/From Warehouse'], inbound_df['One Way Distance To/From Warehouse']], ignore_index=True),
            'avg_gas_price': pd.concat([outbound_df['avg_gas_price'], inbound_df['avg_gas_price']], ignore_index=True),
            'quote': pd.concat([outbound_df['Price Quoted for Outbound'], inbound_df['Price Quoted for Return']], ignore_index=True),
          #   'isMajorCity': pd.concat([outbound_df['isMajorCity'], inbound_df['isMajorCity']], ignore_index=True),
            'shipmentType': pd.concat([outbound_df['Outbound Type of Truck'], inbound_df['Return Type of Truck']], ignore_index=True),
        })
        df.dropna(inplace=True)
        return df
