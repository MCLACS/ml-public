
import numpy as np
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
print('first five rows of x= \n%s' % X[0:6, :])
print('first 150 rows of y= \n%s' % y[0:150])
