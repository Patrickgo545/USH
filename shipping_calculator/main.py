import pandas as pd
from data import df
from regressors import CoefficientModule
import json


# ltl_dataframe = df[df['shipmentType'] == "LTL"]
# coef_labels_ltl = ['pallets', 'weight', 'distance', 'avg_gas_price']
# ltl_regressor  = CoefficientModule(ltl_dataframe,coef_labels_ltl)
# ltl_regressor.TrainRegressor()

# print(ltl_regressor.results_dictionary)


shipment_variables = {
  "shipment_type": { 
      "ltl": ["pallets", "weight", "distance", "avg_gas_price"]
  }
}


def ExtractCoefficients(shipment_type, variable_list):
    coef_labels = variable_list
    
    regressor = CoefficientModule(shipment_type, coef_labels)
    regressor.TrainRegressor()
    
    coefficient_dict = regressor.results_dictionary
    
    return coefficient_dict

ltl = ExtractCoefficients("ltl", shipment_variables["shipment_type"]["ltl"])
print(ltl)