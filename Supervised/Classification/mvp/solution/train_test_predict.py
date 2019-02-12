import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 

import helper as u

mvp_X = u.loadX()
mvp_y = u.loadY()
X_train, X_test, y_train, y_test = train_test_split(mvp_X, mvp_y, random_state = 0)

print('Training...')
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

print('Testing...')
score = knn.score(X_test, y_test)
print('Test set score: {:.2f}'.format(score))

print('Predicting...')
X_new = np.array([ [566,35,108,0.274,0.352,0.539] ])
y_classification = knn.predict(X_new)
print('Prediction: {}->{}'.format(X_new[0], y_classification))
