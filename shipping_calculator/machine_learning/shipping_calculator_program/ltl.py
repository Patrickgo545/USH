from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd
from data import df



class TrainModule:

    def __init__(self, df, coef_labels):
        self.df = df 
        self.coef_labels  = coef_labels
        self.results = None
        self.variables = None
        self.coefficients = None
        self.regressor = self.TrainModule()



    def TrainModule(self):
        self.x_variables = self.df[[self.coef_labels]]

        # DEPENDENT VARIABLE
        y = self.df['quote']

        # SPLIT DATASET
        X_train, X_test, y_train, y_test = train_test_split(self.x_variables,y,test_size=0.2, random_state=0)

        # TRAINING MODEL
        regressor = LinearRegression()
        regressor.fit(X_train,y_train)

        # VALIDATING MODEL
        y_pred = regressor.predict(X_test)
        self.results = pd.DataFrame({'Actual':y_test, 'Predicted':y_pred})

        # EXTRACT COEFFICIENTS
        self.coefficients = self.regressor.coef_
        self.variables = self.x_variables.columns         

        return self.regressor
    

    # def ExtractCoef(self):
    #     coefficients = self.regressor.coef_
    #     variable_names = self.x_variables.columns 

    # TODO: Ship results into CSV for inspections