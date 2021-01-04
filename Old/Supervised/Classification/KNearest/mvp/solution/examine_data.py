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

import helper as u


mvp_X = u.loadX()
mvp_y = u.loadY()
print('First 5 rows of samples:\n{}\n'.format(mvp_X[:5])) 
print('First 5 rows of samples:\n{}\n'.format(mvp_y[:5])) 

# split the data into a training sert and a testing set
X_train, X_test, y_train, y_test = train_test_split(mvp_X, mvp_y, random_state = 0)
print('X_train size: {}'.format(len(X_train)))
print('y_train size: {}'.format(len(y_train)))
print('X_test size: {}'.format(len(X_test)))
print('y_test shape: {}'.format(len(y_test)))


# Let's examine the traning set to see if 
# the features are useful for classifyiung the samples
# start by creating a pandas DataFrame from the training set
iris_dataframe = pd.DataFrame(X_train, columns=['pa', 'hr', 'rbi', 'ba', 'obp', 'slg'])
print('Keys:\n{}'.format(iris_dataframe.keys()))

# now create a scatter matrix and save it to a file
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15), marker='0', s=60, alpha=.8, cmap=mglearn.cm2)
plt.savefig(r"scatter_matrix_iris_training.png")
