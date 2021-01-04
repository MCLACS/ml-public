import sys
sys.path.append('../../modules')

import numpy as np
import matplotlib.pyplot as plt
import functions as f
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = np.loadtxt('CRICK-X.csv',skiprows=1, unpack=False, delimiter=',')
X = f.listTo2DNumPy(x)
y = np.loadtxt('CRICK-Y.csv',skiprows=1, unpack=False, delimiter=',')
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

print('\nTraining...')
lr = LinearRegression().fit(X_train , y_train)
print("lr.coef_: %f" % lr.coef_)
print("lr.intercept_: %f" % lr.intercept_)

print('\nTesting...')
print( "Training set score linear: %.2f" % lr.score( X_train , y_train))
print( "Test set score linear: %.2f" % lr.score(X_test , y_test))

print('\nPredicting...')
freq = float(input("Enter a chirp frequency:"))
X_new_sample = np.array([[freq]])
y_classification = lr.predict(X_new_sample)
print('Prediction: %s->%s' % (X_new_sample[0], y_classification[0]))
