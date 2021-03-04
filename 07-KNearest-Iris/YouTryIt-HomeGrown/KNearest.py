import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# this KMeans algorithm has K fixed to 1
# it will always look for the example
# in the training set that is closest
# 'predict' and use the label of the
# closest node it finds to the determine
# the label for 'predict'
def knearest(X_train, y_train, predict):

	# keeps track of the minimunm distance
	min_dist = 10000

	# keeps track of the index of the closest example
	min_sample_idx = 0

	# for each example in the training set
	for i1 in range(0, len(X_train)):
		print("Training...")
		# compare the training example to 'predict'
		# and find the example that is closet
		# to predict
		#
		# NOTE: the difference between the current
		# example in the training set and predict
		# can be calculated as follows:
		# math.pow((X_train[i1][i2] - predict[i2]), 2)

		# your code goes here...

		# return the predicted label for 'predict'
	return y_train[min_sample_idx]


def main():
	iris_dataset = load_iris()
	X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0)

	total = 0
	correct = 0
	for i in range(0, len(X_test)):
	    ans = knearest(X_train, y_train, X_test[i])
	    total = total + 1
	    if ans == y_test[i]:
	        correct = correct + 1
	print('Score: {:.2f}'.format(correct/total))

main()
