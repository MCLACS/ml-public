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

# Lets scale the features...

# compute the minimum value per feature on the training set (min across rows)
min_on_training=X_train.min(axis=0)
print("Minimum value in training: %s" % min_on_training)
# compute the range of each feature (max - min) on the training set
range_on_training = (X_train - min_on_training).max(axis = 0)
print("Range of training: %s" % range_on_training)

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
