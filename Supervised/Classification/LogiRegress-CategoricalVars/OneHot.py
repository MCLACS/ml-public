import sys
sys.path.append('/home/ubuntu/workspace/utils')

import os 
import mglearn as mglearn
import pandas as pd
from IPython.display import display
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split

# The file has no headers naming the columns, so we pass header=None 
# and provide the column names explicitly in "names" 

adult_path = os.path.join(mglearn.datasets.DATA_PATH,"adult.data")

cols=['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','gender','capital-gain','capital-loss','hours-per-week','native-country' , 'income' ] 
data = pd.read_csv(adult_path,header=None,index_col=False,names=cols)

display(data.head()) 

print (data.gender.value_counts())

print("Original features:\n",data.columns,"\n")
data_dummies = pd.get_dummies(data)
print("Features after get_dummies:\n",data_dummies.columns)

display(data_dummies.head())
 
# loc allows you to access rows and columns using lables and array/slice notation
# loc[row, colum] where row and columns can be slices that are inclusive

# for example, first three rows, all columns from age to occupation_ Transport-moving
features = data_dummies.loc[0:2, 'age' : 'occupation_ Transport-moving'] 
display(features)

# or all rows, all columns from age to occupation_ Transport-moving
features = data_dummies.loc[:, 'age' : 'occupation_ Transport-moving'] 

# Extract NumPy arrays 
X = features.values
y = data_dummies[ 'income_ >50K' ].values 
print ( "X.shape: {} y.shape: {}" . format ( X . shape , y . shape )) 

# Logistic Regression is used when the dependent variable(target) is categorical.
# It is a simple form of classification.
# For example,
# To predict whether an email is spam (1) or (0)
# To predict whether someone will make less than 50k (0) or more than 50k (1)

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)
logreg=LogisticRegression(solver='lbfgs')
logreg.fit(X_train,y_train)
print("Testscore: {:.2f}".format(logreg.score(X_test,y_test)))




