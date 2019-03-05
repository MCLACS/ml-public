import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz 

# use the following commands first:
# sudo pip3 install pydot 
# sudo apt-get install graphviz
import pydot 

cancer = load_breast_cancer() 
X_train , X_test , y_train , y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42) 

print('Training...')
tree1 = DecisionTreeClassifier( random_state = 0 )
tree2 = DecisionTreeClassifier( max_depth = 4, random_state = 0 )
tree1.fit (X_train, y_train ) 
tree2.fit (X_train, y_train ) 

print('Testing...')
print("Accuracy on training set: {:.3f}".format(tree1.score( X_train , y_train)))
print( "Accuracy on test set: {:.3f}".format(tree1.score( X_test , y_test)))
print("Accuracy on training set with pruning: {:.3f}".format(tree2.score( X_train , y_train)))
print( "Accuracy on test set with pruning: {:.3f}".format(tree2.score( X_test , y_test)))

print( "Feature importances: \n {}".format (tree2.feature_importances_ )) 


# now create a bar chart and save it to a file
n_features = cancer.data.shape[ 1 ] 
plt.barh( range( n_features ), tree2.feature_importances_ , align = 'center' ) 
plt.yticks( np.arange( n_features ), cancer.feature_names ) 
plt.xlabel( "Feature importance" ) 
plt.ylabel( "Feature" )
plt.ylim ( 1 , n_features ) 
plt.savefig(r"feature_importance.png",bbox_inches='tight')

export_graphviz(tree2 , out_file = "tree.dot", class_names = [ "malignant" , "benign" ], feature_names = cancer.feature_names , impurity = False , filled = True ) 

(graph,) = pydot.graph_from_dot_file('./tree.dot')
graph.write_png('./tree.png')

# with open ( "tree.dot" ) as f: 
#     dot_graph = f.read () 
#     display(graphviz. Source( dot_graph )) 


