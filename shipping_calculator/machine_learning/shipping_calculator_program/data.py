import pandas as pd
import difflib


# FUNCTIONS

def isMajorCity(city):
    majorCities = ["new york", "nyc", "ny", "chicago", "san francisco", "san fran", "los angeles", "la"]
    
    closest_match = difflib.get_close_matches(city, majorCities)
    if closest_match and closest_match[0] == city.lower():
         return True

    return False



def isShipmentOnWeekend(shipment_date):
     if shipment_date.weekday() in [5,6]:
          return True
     else: 
          return False
     



# IMPORT CSV'S
     
# SHIPPING DASHBOARD CSV
shipments_df = pd.read_csv("shipments_2023.csv")

# GAS PRICE AVERAGES CSV
monthly_gas_averages = pd.read_csv("./gas_averages - U.S._All_Grades_All_Formulations_Retail_Gasoline_Prices (2) (1).csv")

# CONVERT DATE COLUMN IN SHIPMENTS_DS TO DATETIME
shipments_df['Project Date'] = pd.to_datetime(shipments_df['Project Date'], format='%Y-%m-%d')

# ADJUST PROJECT DATE TO MATCH MONTHLY GAS AVG & MERGE
shipments_df['month_year'] = shipments_df['Project Date'].dt.month.astype(str) + '/' + shipments_df['Project Date'].dt.year.astype(str)
shipments_df = pd.merge(shipments_df, monthly_gas_averages, how='left', left_on='month_year', right_on='Month', suffixes=('_shipments', '_gas'))

shipments_df = shipments_df.rename(columns={'U.S. All Grades All Formulations Retail Gasoline Prices Dollars per Gallon': 'avg_gas_price'})




