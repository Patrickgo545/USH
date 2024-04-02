import pandas as pd
from ltl import TrainModule
from data import df

coef_labels_ltl = ['pallets', 'weight', 'distance', 'avg_gas_price']



ltl = TrainModule(df=df, coef_labels=coef_labels_ltl)


