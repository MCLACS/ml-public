# ------------------------------------------------------
# This file is used to explore the structure and values
# of the sample iris datafile included with sklearn
# ------------------------------------------------------
import sys
sys.path.append('/home/ubuntu/workspace/utils')

import mglearn as mglearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

X = np.loadtxt('mvp_X.csv',skiprows=0, unpack=False, delimiter=',')
y = np.loadtxt('mvp_y.csv',skiprows=0, unpack=False, delimiter=',')

print(X);
# split the data into a training sert and a testing set
X_train , X_test , y_train , y_test = train_test_split(X, y, stratify=y, random_state=42) 
print('X_train shape: {}'.format(X_train.shape))
print('y_train shape: {}'.format(y_train.shape))
print('X_test shape: {}'.format(X_test.shape))
print('y_test shape: {}'.format(y_test.shape))

