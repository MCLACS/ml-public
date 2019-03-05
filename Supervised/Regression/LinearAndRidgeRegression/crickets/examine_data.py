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

# CRICK-X.csv
# Columns: Chirp Freq

# CRICK-Y.csv
# Columns: Temp F
X = np.loadtxt('CRICK-X.csv',skiprows=1, unpack=False, delimiter=',')
l = []
for i in range(len(X)):
    l.append([X[i]]);
X = np.array(l);
y = np.loadtxt('CRICK-Y.csv',skiprows=1, unpack=False, delimiter=',')

print('x-values shape:{}'.format(X.shape)) 
print('y-values shape:{}'.format(y.shape)) 
print('First 5 x-values:{}'.format(X[:5])) 
print('First 5 y-values{}'.format(y[:5])) 

# split the data into a training sert and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 54)
print('X_train shape: {}'.format(X_train.shape))
print('y_train shape: {}'.format(y_train.shape))
print('X_test shape: {}'.format(X_test.shape))
print('y_test shape: {}'.format(y_test.shape))



