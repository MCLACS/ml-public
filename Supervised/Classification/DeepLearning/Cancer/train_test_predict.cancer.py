#################################################
# Try first as is...
# Next add a second hidden layer
# Finally scale it 
#################################################

import sys
sys.path.append('/home/ubuntu/workspace/utils')

import numpy as np
import matplotlib.pyplot as plt
import mglearn as mglearn
from sklearn.datasets import load_breast_cancer 
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler 

cancer = load_breast_cancer() 
X = cancer.data
y = cancer.target

# scaler = MinMaxScaler() 
# X = scaler.fit_transform(X) 

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 8)

print('Training...')
mlp = MLPClassifier(solver = 'lbfgs' , random_state = 42, hidden_layer_sizes = [ 10 ], activation = 'relu') #tanh 
mlp.fit( X_train , y_train ) 

print('Testing...')
score = mlp.score(X_train, y_train)
print('Train set score: {:.2f}'.format(score))
score = mlp.score(X_test, y_test)
print('Test set score: {:.2f}'.format(score))

