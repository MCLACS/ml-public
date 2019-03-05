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

# iris_dataset is a Bunch datatype -- similar to a dictionary
cancer = load_breast_cancer() 

print('Keys:\n{}'.format(cancer.keys())) 
# targets are the iris we are trying to identify
print('Targets:\n{}'.format(cancer['target_names'])) 
# features are the attributes we use to identify
print('Features:\n{}'.format(cancer['feature_names'])) 
# the data is stored as a NumPy array (150, 4)
print('Shape of data:\n{}'.format(cancer['data'].shape)) 
# each sample (row) has four measurements, one for each feature
print('First 5 rows of data:\n{}'.format(cancer['data'][:5])) 
# target is a one-dim NumPy array encoded (0,1,2) (150,) -- this represents the iris classificiations
print('Shape of targets:\n{}'.format(cancer['target'].shape)) 
# targets are encoded (0,1,2), one row (label or classification) for each sample (row) in data
print('Targets:\n{}'.format(cancer['target'])) 


# split the data into a training sert and a testing set
X_train , X_test , y_train , y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42) 
print('X_train shape: {}'.format(X_train.shape))
print('y_train shape: {}'.format(y_train.shape))
print('X_test shape: {}'.format(X_test.shape))
print('y_test shape: {}'.format(y_test.shape))

