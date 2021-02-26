import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# load the data...
iris = load_iris()
X = iris.data
y = iris.target
featureNames =iris.feature_names
labelNames = iris.target_names

# print features and labels...
print("Features %s" % featureNames)
print("Labels %s" % labelNames)

# create the train and test sets for X and y
# traning has 67% of the rows and test has 33% of the rows...
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state = 12)

# print shape of data sets...
print('Entire set shape= %s' % str(X.shape))
print('Training set shape= %s' % str(X_train.shape))
print('Test set shape= %s' % str(X_test.shape))

# train the decision tree algorithm...
print('Training...')
tree2 = tree.DecisionTreeClassifier(max_depth = 10, random_state = 32)
tree2.fit (X_train, y_train)

# test it...
print('Testing...')
print("Accuracy on training set with pruning: {:.3f}".format(tree2.score( X_train , y_train)))
print( "Accuracy on test set with pruning: {:.3f}".format(tree2.score( X_test , y_test)))
print( "Feature importances: \n {}".format (tree2.feature_importances_ ))

# now create a bar chart
plt.barh( range( len(featureNames) ), tree2.feature_importances_ , align = 'center' )
plt.yticks( np.arange( len(featureNames) ), featureNames )
plt.xlabel( "Feature importance" )
plt.ylabel( "Feature" )
plt.ylim ( 0 , len(featureNames) )
plt.subplots_adjust(left=0.28, right=0.9, top=0.9, bottom=0.1)
plt.show()

# plot the tree to png...
plt.figure(dpi=1200)
tree.plot_tree(tree2)
plt.savefig(r"tree.png",bbox_inches='tight')
