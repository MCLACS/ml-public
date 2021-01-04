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
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

X, y = mglearn.datasets.load_extended_boston()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)


print('Training...')
# different values of alpha (regularization)
rAlphaDefault = Ridge(alpha=1.0).fit(X_train , y_train) 
rAlphaSmall = Ridge(alpha=0.1).fit(X_train , y_train) 
rAlphaLarge = Ridge(alpha=10).fit(X_train , y_train) 
lr = LinearRegression().fit(X_train , y_train) 

print("lr.coef_: {}".format(lr.coef_)) 
print("rAlphaDefault.coef_: {}".format(rAlphaDefault.coef_)) 
print("rAlphaSmall.coef_: {}".format(rAlphaSmall.coef_)) 
print("rAlphaLarge.coef_: {}".format(rAlphaLarge.coef_)) 

# linear regression overfits 
# ridge restricts the magnitude of the coefficients 
# so that each feature has less weight
# print('Testing...')
print( "Training set score linear: {:.2f}".format(lr.score( X_train , y_train))) 
print( "Test set score linear: {:.2f}".format(lr.score(X_test , y_test))) 
print( "Training set score ridge with alpha 1: {:.2f}".format(rAlphaDefault.score( X_train , y_train))) 
print( "Test set score ridge with alpha 1: {:.2f}".format(rAlphaDefault.score(X_test , y_test))) 
print( "Training set score with alpha 0.1: {:.2f}".format(rAlphaSmall.score( X_train , y_train))) 
print( "Test set score with alpha 0.1: {:.2f}".format(rAlphaSmall.score(X_test , y_test))) 
print( "Training set score with alpha 10: {:.2f}".format(rAlphaLarge.score( X_train , y_train))) 
print( "Test set score with alpha 10: {:.2f}".format(rAlphaLarge.score(X_test , y_test))) 

# visualize coefficient magnitudes of Linear and Ridge
# visualize impact of alpha on Ridge  
plt.plot ( rAlphaDefault.coef_ , 's' , label = "Ridge alpha=1" ) 
plt.plot ( rAlphaLarge.coef_ , '^' , label = "Ridge alpha=10" ) 
plt.plot ( rAlphaSmall.coef_ , 'v' , label = "Ridge alpha=0.1" ) 
plt.plot ( lr.coef_ , 'o' , label = "LinearRegression" ) 
plt.xlabel( "Coefficient index" ) 
plt.ylabel( "Coefficient magnitude" ) 
plt.hlines ( 0 , 0 , len (lr.coef_ )) 
plt.ylim (-25,25) 
plt.legend() 
plt.savefig(r"differentAlpha.png")

# print('Predicting...')
# X_new_sample = np.array([ X_test[0] ])
# y_classification = lr.predict(X_new_sample)
# print('Prediction: {}->{}'.format(X_new_sample[0], y_classification[0]))
