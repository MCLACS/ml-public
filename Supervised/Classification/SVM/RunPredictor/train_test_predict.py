import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
 
X = np.loadtxt('RunPredictor_X.csv',skiprows=1, unpack=False, delimiter=',')
y = np.loadtxt('RunPredictor_y.csv',skiprows=1, unpack=False, delimiter=',')
X_train , X_test , y_train , y_test = train_test_split(X, y, random_state=42) 


print('Training...')
svc2 = SVC(kernel='rbf', C=1, gamma='auto') # change c to 10 for better fit
svc2.fit(X_train, y_train) 

print('Testing...')
print( "Accuracy on training set before scale: {:.2f}".format(svc2.score(X_train, y_train))) 
print( "Accuracy on test set before scale: {:.2f}".format(svc2.score(X_test, y_test ))) 


min_on_training=X_train.min(axis=0) 
range_on_training = (X_train - min_on_training).max(axis = 0) 
X_train_scaled = ( X_train - min_on_training ) / range_on_training 
X_test_scaled = ( X_test - min_on_training ) / range_on_training 

plt.boxplot( X_train_scaled , manage_xticks = False ) 
plt.yscale( "symlog" ) 
plt.xlabel( "Feature index" ) 
plt.ylabel ( "Feature magnitude" ) 
plt.savefig(r"feature_magnitude_after_scale.png",bbox_inches='tight')

print('Training...')
svc2 = SVC(kernel='rbf', C=1, gamma='auto') # change c to 10 for better fit
svc2.fit(X_train_scaled, y_train) 

print('Testing...')
print( "Accuracy on training set: {:.2f}".format(svc2.score(X_train_scaled, y_train))) 
print( "Accuracy on test set: {:.2f}".format(svc2.score(X_test_scaled, y_test ))) 




