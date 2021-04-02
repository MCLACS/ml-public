#################################################
# Try first as is...
# Next add a second hidden layer
# Finally scale it
#################################################
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler

# cancer = load_breast_cancer()
# X = cancer.data
# y = cancer.target

train = np.loadtxt('handwriting.csv',skiprows=1, unpack=False, delimiter=',')

y = train[:, 0]
X = train[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state = 12)

# scaler = MinMaxScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.fit_transform(X_test)

print('Training...')
# lbfgs faster on small datasets, Adam for largers datasets
mlp = MLPClassifier(solver = 'lbfgs' , random_state = 42, hidden_layer_sizes = [], activation = 'tanh') #tanh
#mlp = MLPClassifier(solver = 'adam' , random_state = 42, hidden_layer_sizes = [ 100 ], activation = 'tanh') #tanh
mlp.fit( X_train , y_train )

print('Testing...')
score = mlp.score(X_train, y_train)
print('Train set score: {:.2f}'.format(score))
score = mlp.score(X_test, y_test)
print('Test set score: {:.2f}'.format(score))

print('\nPredicting...')
plt.matshow(X_test[3].reshape(28,28))
plt.show()
y_classification = mlp.predict([X_test[3]])
print('Prediction: %s' % y_classification[0])
