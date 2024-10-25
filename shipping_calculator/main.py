import pandas as pd
from data import df
from regressors import CoefficientModule
import json


shipment_variables = {
    "ltl": ["pallets", "weight", "distance", "avg_gas_price"]
}


def ExtractCoefficients(shipment_type, variable_list):
    coef_labels = variable_list
    
    regressor = CoefficientModule(shipment_type, coef_labels)
    regressor.TrainRegressor("LTL")
    
    coefficient_dict = regressor.results_dictionary
    
    return coefficient_dict

shipment_var = shipment_variables["ltl"]
ltl = ExtractCoefficients("LTL", shipment_var)
print(ltl)