import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 22)

print('Training...')
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

print('Testing...')
score = knn.score(X_test, y_test)
print('Test set score: {:.2f}'.format(score))

print('Predicting...')
s_l  = float(input("Enter sepal_length: "))
s_w  = float(input("Enter sepal_width: "))
p_l  = float(input("Enter petal_length: "))
p_w  = float(input("Enter petal_width: "))
X_new_iris = np.array([ [s_l, s_w, p_l, p_w] ])
y_classification = knn.predict(X_new_iris)
print('Prediction: %s->%s' % (X_new_iris[0], iris_dataset['target_names'][y_classification[0]]))
