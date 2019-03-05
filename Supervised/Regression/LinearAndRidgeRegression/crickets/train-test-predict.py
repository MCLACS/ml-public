# ------------------------------------------------------
# This file is used to explore the structure and values
# of the sample wave datafile for use with linear 
# regression y = a1(x1) + a2(x2) + ... + b 
# ------------------------------------------------------
import sys
sys.path.append('/home/ubuntu/workspace/utils')

import mglearn as mglearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

X = np.loadtxt('CRICK-X.csv',skiprows=1, unpack=False, delimiter=',')
l = []
for i in range(len(X)):
    l.append([X[i]]);
X = np.array(l);
y = np.loadtxt('CRICK-Y.csv',skiprows=1, unpack=False, delimiter=',')
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)


print('Training...')
lr = LinearRegression().fit(X_train , y_train) 
rr = Ridge(alpha=0.1).fit(X_train , y_train) 
print("lr.coef_: {}".format(lr.coef_)) 
print("lr.intercept_: {}".format(lr.intercept_)) 
print("rr.coef_: {}".format(rr.coef_)) 
print("rr.intercept_: {}".format(rr.intercept_)) 



print('Testing...')
print( "Training set score linear: {:.2f}".format(lr.score( X_train , y_train))) 
print( "Test set score linear: {:.2f}".format(lr.score(X_test , y_test))) 

print('Testing...')
print( "Training set score ridge: {:.2f}".format(rr.score( X_train , y_train))) 
print( "Test set score ridge: {:.2f}".format(rr.score(X_test , y_test))) 


# print('Predicting...')
# X_new_sample = np.array([[ 159,692,59,123,132,2,12.30,23.60,0.281,0.376,0.631]])
# y_classification = lr.predict(X_new_sample)
# print('Prediction: {}->{}'.format(X_new_sample[0], y_classification[0]))
