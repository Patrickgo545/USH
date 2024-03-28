from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from data import df




class LtlModule:
    def __init__(self, df):
        self.df = df 

    def TrainModule(self):
        X = df[['pallets', 'weight', 'distance', 'avg_gas_price']]

        # DEPENDENT VARIABLE
        y = df['quote']

        # SPLIT DATASET
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=0)

        # TRAINING MODEL
        regressor = LinearRegression()
        regressor.fit(X_train,y_train)

        # VALIDATING MODEL
        y_pred = regressor.predict(X_test)

        return regressor


#coefficients =     