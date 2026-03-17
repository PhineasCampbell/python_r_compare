'''
This is a python script to test the difference between the output of the estimates of the linear 
model produced by skikit-learn and R.  It runs 10,000 simulation, generates a 2 by 20 model, fits the 
model, then calls R to fit the same model and compares the output.
'''
import subprocess
import os
import sys
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
DATA_FILE = 'data.csv'
RESULTS_FILE = 'results.csv'
R_RESULTS_FILE = 'r_results.csv'
NBR_SIMULATIONS = 10000
# Make sure we have the required r script
R_SCRIPT = '/home/phineas/python_r_compare_two/python_r_compare/simulate_r.r'
if not os.path.exists(R_SCRIPT):
    print('Cannot locate R script')
    sys.exit()
# If the the results csv files exist then delete them
if os.path.exists(R_RESULTS_FILE):
    os.remove(R_RESULTS_FILE)
if os.path.exists(RESULTS_FILE):
    os.remove(RESULTS_FILE)
if os.path.exists(DATA_FILE):
    os.remove(DATA_FILE)
output = np.empty((NBR_SIMULATIONS,6))
data_store = dict()
for i in range(NBR_SIMULATIONS):
    # Generate the intercept
    intercept = np.random.randint(10,size = (1))[0]
    # Generate b_1
    b_1 = (np.random.randint(20,size = (1))[0] - 10)/10
    # Generate b_2
    b_2 = (np.random.randint(20,size = (1))[0] - 10)/10
    # Generate X
    X = np.random.randint(60, size=(60,2))
    # Form y
    y = intercept + b_1 * X[:,0] + b_2 * X[:,-1] + np.random.normal(size=(60))
    # Fit the linear model
    result = LinearRegression().fit(X, y)
    # Extract the intercept
    intercept_hat = result.intercept_
    # Extract b_1
    b_1_hat = result.coef_[0]
    # Extract b_2
    b_2_hat = result.coef_[1]
    # Save the estimates
    output[i] = np.array([intercept, intercept_hat, b_1, b_1_hat, b_2, b_2_hat])
    # Now save the data
    data_store['y_' + str(i)] = y
    data_store['x_1_' +str(i)] = X[:,0]
    data_store['x_2_' +str(i)] = X[:,-1]
data = pd.DataFrame.from_dict(data_store)
data.to_csv(DATA_FILE, index=False)
results = pd.DataFrame(output, columns=['intercept', 'intercept_hat', 'b_1', 'b_1_hat', 'b_2', 'b_2_hat'])
results.to_csv(RESULTS_FILE, index=False)
# Call R
try:
    subprocess.run(['/usr/bin/Rscript', R_SCRIPT], check=True)
except FileNotFoundError:
    print('Could not find RScript')
    sys.exit()
# Load the r results
r_results = pd.read_csv(R_RESULTS_FILE)
intercept_diff = np.array(results['intercept_hat']) -  np.array(r_results['intercept_hat'])
print("Maximum value of intercept difference:", intercept_diff.max())
print("Minimum value of intercept difference:", intercept_diff.min())
b_1_diff = np.array(results['b_1_hat']) -  np.array(r_results['b_1_hat'])
print("Maximum value of b1 difference:", b_1_diff.max())
print("Minimum value of b1 differene:", b_1_diff.min())
b_2_diff = np.array(results['b_2_hat']) -  np.array(r_results['b_2_hat'])
print("Maximum value of b2 difference:", b_2_diff.max())
print("Minimum value of b2 difference:", b_2_diff.min())
