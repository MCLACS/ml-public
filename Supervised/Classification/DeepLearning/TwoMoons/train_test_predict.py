import sys
sys.path.append('/home/ubuntu/workspace/utils')

import numpy as np
import matplotlib.pyplot as plt
import mglearn as mglearn
from sklearn.datasets import make_moons 
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

X, y = make_moons() 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 3)

print('Training...')
mlp = MLPClassifier(solver = 'lbfgs' , random_state = 42, hidden_layer_sizes = [ 10 ], activation = 'tanh') #tanh 
mlp.fit( X_train , y_train ) 

print('Testing...')
score = mlp.score(X_train, y_train)
print('Train set score: {:.2f}'.format(score))
score = mlp.score(X_test, y_test)
print('Test set score: {:.2f}'.format(score))

print('Generating Boundary Plot...')
mglearn.plots.plot_2d_separator(mlp,X_train,fill=True,alpha=.3)
mglearn.discrete_scatter(X_train[:,0],X_train[:,1],y_train)
plt.xlabel("Feature0")
plt.ylabel("Feature1")
plt.savefig(r"boundary.png")
