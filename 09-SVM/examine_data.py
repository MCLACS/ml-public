# ------------------------------------------------------
# This file is used to explore the structure and values
# of the sample iris datafile included with sklearn
# ------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()

print('Label Names:\n{}'.format(cancer['target_names']))
print('Feature Names:\n{}'.format(cancer['feature_names']))
print('Shape of examples:\n{}'.format(cancer['data'].shape))
print('First 5 rows of examples:\n{}'.format(cancer['data'][:5]))
print('Shape of lables:\n{}'.format(cancer['target'].shape))
print('Label Values:\n{}'.format(cancer['target']))


# split the data into a training sert and a testing set
X_train , X_test , y_train , y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)
print('X_train shape: {}'.format(X_train.shape))
print('y_train shape: {}'.format(y_train.shape))
print('X_test shape: {}'.format(X_test.shape))
print('y_test shape: {}'.format(y_test.shape))

# we have an issue because range of features values is very wide
# this is a problem for most machine learning algorithms, but
# it is a major proboem for SVM
plt.boxplot( X_train, showfliers = False )
plt.yscale( "symlog" )
plt.xlabel( "Feature index" )
plt.ylabel ( "Feature magnitude" )
plt.savefig(r"feature_magnitude.png",bbox_inches='tight')
