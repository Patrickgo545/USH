import pandas as pd
from data import df
from regressors import CoefficientModule
import json

result = {}

shipment_variables = {
    "LTL": ["pallets", "weight", "distance", "avg_gas_price"],
    "FTL": ["weight", "distance", "avg_gas_price"],
    "Box Truck": ["pallets", "weight", "distance", "avg_gas_price"],
    "Sprinter Van": ["distance", "avg_gas_price"]
}


def ExtractCoefficients(shipment_type, variable_list):
    coef_labels = variable_list
    
    regressor = CoefficientModule(shipment_type, coef_labels)
    regressor.TrainRegressor("LTL")
    
    coefficient_dict = regressor.results_dictionary
    
    return coefficient_dict


# shipment_var = shipment_variables["LTL"]
# ltl = ExtractCoefficients("LTL", shipment_var)
# print(ltl)

for shipment_type, variables in shipment_variables.items():
    coefficients = ExtractCoefficients(shipment_type, variables)
    
    result[shipment_type] = coefficients
    
print(result)