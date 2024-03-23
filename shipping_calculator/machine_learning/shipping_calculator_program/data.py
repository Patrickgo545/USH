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



# CREATE DATAFRAME
# CONVERT DATE COLUMN IN SHIPMENTS_DS TO DATETIME
shipments_df['Project Date'] = pd.to_datetime(shipments_df['Project Date'], format='%Y-%m-%d')

# MERGE NATIONAL GAS PRICE AVERAGES WITH PROJECT DATE
shipments_df['month_year'] = shipments_df['Project Date'].dt.month.astype(str) + '/' + shipments_df['Project Date'].dt.year.astype(str)
shipments_df = pd.merge(shipments_df, monthly_gas_averages, how='left', left_on='month_year', right_on='Month')

# APPLY FORMULAS
shipments_df['isMajorCity'] = shipments_df['HP City'].apply(isMajorCity)
# TODO: INCLUDE MAJOR CITY 
# TODO: INCLUDE IS SHIPMENT ON WEEKEND

# OUTBOUND
outbound_columns = ['Outbound # of Pallets', 'Outbound Total Weight (in lbs)', 'Outbound Type of Truck', 'Price Quoted for Outbound', 'One Way Distance To/From Warehouse', \
                    'U.S. All Grades All Formulations Retail Gasoline Prices Dollars per Gallon', 'Outbound Type of Truck', 'Load In Date & Time', 'isMajorCity']
outbound_df = shipments_df[outbound_columns].copy()
# outbound_df['shipmentOnWeekend'] = outbound_df['Load In Date & Time'].apply(isShipmentOnWeekend)
# print(outbound_df['shipmentOnWeekend'])


# INBOUND
inbound_columns = ['Return # of Pallets', 'Return Total Weight', 'Return Type of Truck', 'Price Quoted for Return', 'One Way Distance To/From Warehouse', \
                   'U.S. All Grades All Formulations Retail Gasoline Prices Dollars per Gallon', 'Return Type of Truck', 'Load Out Date & Time', 'isMajorCity']
inbound_df = shipments_df[inbound_columns].copy()

#CREATE WORKING DF
df = pd.DataFrame()
df['pallets'] = pd.concat([outbound_df['Outbound # of Pallets'], inbound_df['Return # of Pallets']], ignore_index=True)
df['weight'] = pd.concat([outbound_df['Outbound Total Weight (in lbs)'], inbound_df['Return Total Weight']], ignore_index=True)
df['distance'] = pd.concat([outbound_df['One Way Distance To/From Warehouse'], inbound_df['One Way Distance To/From Warehouse']], ignore_index=True)
df['avg_gas_price'] = pd.concat([outbound_df['U.S. All Grades All Formulations Retail Gasoline Prices Dollars per Gallon'], \
                                 inbound_df['U.S. All Grades All Formulations Retail Gasoline Prices Dollars per Gallon']], ignore_index=True)
df['quote'] = pd.concat([outbound_df['Price Quoted for Outbound'], inbound_df['Price Quoted for Return']], ignore_index=True)
df['isMajorCity'] = pd.concat([outbound_df['isMajorCity'], inbound_df['isMajorCity']], ignore_index=True)

# TODO: df - on weekend



# CLEAN UP COLUMNS
df['weight'] = df['weight'].str.replace(',', '').str.replace(' lbs', '').astype(int)
df['distance'] = df['distance'].str.replace(',', '').str.replace(' miles', '').astype(float)
df['quote'] = df['quote'].str.replace("$", '').str.replace(',', '').astype(float)
# df['pallets'].to_csv('test', index=False)
df['pallets'] = df['pallets'].astype(float)

df = df.dropna(axis=0)

# OLD CALCULATOR 
# df["Old Calculator"] = (((df["distance"] * .114 + 105) * df["pallets"]) + 150 + 22.5)

# SHOW RESULTS
