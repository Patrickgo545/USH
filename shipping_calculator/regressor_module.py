from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd
from data import df



class Regressor:

    def __init__(self, shipment_type, coef_labels):
        self.full_df = df

        self.coef_labels = coef_labels
        self.x_variables = None
        self.results = None
        self.variables = None
        self.coefficients = coef_labels
        self.results_dictionary = {}
        self.regressor = None
        self.intercept = None



    def TrainRegressor(self, shipment_type):
        
        working_df = self.full_df[self.full_df['shipmentType'] == shipment_type]
        self.x_variables = working_df[self.coef_labels]
        
        # DEPENDENT VARIABLE
        y = working_df['quote']

        # SPLIT DATASET
        X_train, X_test, y_train, y_test = train_test_split(self.x_variables,y,test_size=0.2, random_state=0)

        # TRAINING MODEL
        self.regressor = LinearRegression()
        self.regressor.fit(X_train,y_train)
        self.intercept = self.regressor.intercept_

        # VALIDATING MODEL
        y_pred = self.regressor.predict(X_test)
        self.results = pd.DataFrame({'Actual':y_test, 'Predicted':y_pred})

        # EXTRACT COEFFICIENTS
        self.coefficients = self.regressor.coef_
        self.variables = self.x_variables.columns  
        
        
        self.results_dictionary = {variable:coef for variable, coef in zip(self.variables, self.coefficients)}       