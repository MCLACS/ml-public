import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
 

cancer = load_breast_cancer() 
X_train , X_test , y_train , y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42) 

print('Training...')
svc = SVC(kernel='rbf', C=1, gamma='auto')
svc.fit(X_train, y_train) 

print('Testing...')
print( "Accuracy on training set: {:.2f}".format(svc.score(X_train, y_train))) 
print( "Accuracy on test set: {:.2f}".format(svc.score(X_test, y_test ))) 

# we have an issue because range of features values is very wide
# this is a problem for most machine learning algorithms, but
# it is a major proboem for SVC

plt.boxplot( X_train , manage_xticks = False ) 
plt.yscale( "symlog" ) 
plt.xlabel( "Feature index" ) 
plt.ylabel ( "Feature magnitude" ) 
plt.savefig(r"feature_magnitude.png",bbox_inches='tight')

# Time to learn how to scale factors...

# compute the minimum value per feature on the training set 
min_on_training=X_train.min(axis=0) 
print(min_on_training)
# compute the range of each feature (max - min) on the training set
range_on_training = (X_train - min_on_training).max(axis = 0) 
print(range_on_training)

# example of scaling all feature values so they are between 0 and 1
# 50
# 10
# 1
# max = 50, min = 1
# (50-1)/ (50-1) = 1
# (40-1)/(50-1) = 0.796
# (10-1)/(50-1) = 0.184
# (1-1)/(50-1) = 0

# subtract the min, and divide by range 
# afterward, min=0 and max=1 for each feature 
X_train_scaled = ( X_train - min_on_training ) / range_on_training 
X_test_scaled = ( X_test - min_on_training ) / range_on_training 
print("Minimum for each feature \n {}".format( X_train_scaled .min( axis = 0 ))) 
print ("Maximum for each feature \n {}".format( X_train_scaled.max( axis = 0 ))) 

print('Training...')
svc2 = SVC(kernel='rbf', C=1, gamma='auto') # change c to 10 for better fit
svc2.fit(X_train_scaled, y_train) 

print('Testing...')
print( "Accuracy on training set: {:.2f}".format(svc2.score(X_train_scaled, y_train))) 
print( "Accuracy on test set: {:.2f}".format(svc2.score(X_test_scaled, y_test ))) 




