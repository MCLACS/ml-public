import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 

iris_dataset = load_iris() 
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0)

print('Training...')
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

print('Testing...')
score = knn.score(X_test, y_test)
print('Test set score: {:.2f}'.format(score))

print('Predicting...')
X_new_iris = np.array([ [5, 2.9, 1, 0.2] ])
y_classification = knn.predict(X_new_iris)
print('Prediction: {}->{}'.format(X_new_iris[0], iris_dataset['target_names'][y_classification[0]]))
