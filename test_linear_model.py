'''
A basic Python script to test the functionality of the linear model fit of sci
'''
import pandas as pd
from sklearn.linear_model import LinearRegression
# Read the data 
data = pd.read_csv('data.csv')
X = data[['x_1','x_2']].copy()
y = data['y'].copy()
# Fit the linear model
result = LinearRegression().fit(X,y)
# Print the intercept
print('Intercept:', result.intercept_)
# Print the parameter on x_1
print('Parameter on x_1:', result.coef_[0])
# Print the parameter on x_2 
print('Parameter on x_2:', result.coef_[1])




