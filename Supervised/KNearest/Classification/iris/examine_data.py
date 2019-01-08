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
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# iris_dataset is a Bunch datatype -- similar to a dictionary
iris_dataset = load_iris() 
print('Keys:\n{}'.format(iris_dataset.keys())) 
# targets are the iris we are trying to identify
print('Targets:\n{}'.format(iris_dataset['target_names'])) 
# features are the attributes we use to identify
print('Features:\n{}'.format(iris_dataset['feature_names'])) 
# the data is stored as a NumPy array (150, 4)
print('Shape of data:\n{}'.format(iris_dataset['data'].shape)) 
# each sample (row) has four measurements, one for each feature
print('First 5 rows of data:\n{}'.format(iris_dataset['data'][:5])) 
# target is a one-dim NumPy array encoded (0,1,2) (150,) -- this represents the iris classificiations
print('Shape of targets:\n{}'.format(iris_dataset['target'].shape)) 
# targets are encoded (0,1,2), one row (label or classification) for each sample (row) in data
print('Targets:\n{}'.format(iris_dataset['target'])) 
for x in range(0,3): # you can use the code to find the label 
    print('Target label for code {}: {}'.format(x, iris_dataset['target_names'][x])) 

# split the data into a training sert and a testing set
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0)
print('X_train shape: {}'.format(X_train.shape))
print('y_train shape: {}'.format(y_train.shape))
print('X_test shape: {}'.format(X_test.shape))
print('y_test shape: {}'.format(y_test.shape))


# Let's examine the traning set to see if 
# the features are useful for classifyiung the samples
# start by creating a pandas DataFrame from the training set
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
print('Keys:\n{}'.format(iris_dataframe.keys()))

# now create a scatter matrix and save it to a file
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15), marker='0', s=60, alpha=.8, cmap=mglearn.cm3)
plt.savefig(r"scatter_matrix_iris_training.png")
