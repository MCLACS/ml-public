
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# load data...
iris = load_iris()
X = iris.data
y = iris.target
featureNames =iris.feature_names
labelNames = iris.target_names

#print features and labels...
print("Features %s" % featureNames)
print("Labels %s" % labelNames)

# print shape...
print('X shape: %s' % str(X.shape))
print('y shape: %s' % str(y.shape))

# print data...
print('first five rows of X= \n%s' % X[0:6, :])
print('first 150 rows of y= \n%s' % y[0:150])

# Let's examine the data to see if
# the features are useful for classifyiung the samples
# start by creating a pandas DataFrame from the training set
iris_dataframe = pd.DataFrame(X, columns=featureNames)

# now create a scatter matrix and save it to a file
pd.plotting.scatter_matrix(iris_dataframe, c=y, figsize=(15,15), marker='0', s=60, alpha=.8)
plt.savefig(r"scatter_matrix_iris_training.png")
