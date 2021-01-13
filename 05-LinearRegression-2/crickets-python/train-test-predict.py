import sys
sys.path.append('../../modules')

import numpy as np
import matplotlib.pyplot as plt
import functions as f
from sklearn.linear_model import LinearRegression

all = np.loadtxt('CRICK.csv',skiprows=1, unpack=False, delimiter=',')

# shuffle the rows so that we get random training and test sets...
rng = np.random.default_rng(seed=99)
rng.shuffle(all)

# slice so x is the first column and y is the second column
x = all[:, 0]
y = all[:, 1]

# in this example there is only one feature
# but the linear regression algorithm still wants
# X to be a 2D numpy array, so we convert it here,
# this is not necessary if X has more than one feature...
X = f.listTo2DNumPy(x)

# create the train and test sets for X and y
# traning has 75% of the rows and test has 25% of the rows...
train_size = int(X.shape[0]*0.75)
test_size=int(X.shape[0]-train_size)

X_train = X[0:train_size, :]
X_test = X[train_size:, :]
y_train = y[0:train_size]
y_test = y[train_size:]

print('Entire set shape= %s' % str(X.shape))
print('Training set shape= %s' % str(X_train.shape))
print('Test set shape= %s' % str(X_test.shape))

print('\nExcel results...')
print("Excel Coef: %f" % 0.8918)
print("Excel Intercept: %f" % 40.025)
print( "Excel score linear: %.2f" % 0.9609)

print('\nTraining results...')
# train the regression algorithm...
lr = LinearRegression().fit(X_train , y_train)
print("lr.coef_: %s" % lr.coef_)
print("lr.intercept_: %f" % lr.intercept_)
print( "Training set score linear: %.2f" % lr.score( X_train , y_train))

print('\nTesting results...')
print( "Test set score linear: %.2f" % lr.score(X_test , y_test))

print('\nPredicting...')
freq = float(input("Enter a chirp frequency:"))
X_new_sample = np.array([[freq]])
y_classification = lr.predict(X_new_sample)
print('Prediction: %s->%s' % (X_new_sample[0], y_classification[0]))

# plot the points...
plt.scatter(x, y)

# set the labels...
plt.xlabel('Chirp Freq')
plt.ylabel('Temp')
plt.title('Crickets Chirp vs. Temp')

# set the limits of the plotspace...
plt.xlim(left=0, right=x.max()+ 10)
plt.ylim(bottom=0, top=y.max()+ 10)

# plot the line...
x_values = [x.min(), x.max()]
y_values = [lr.intercept_ + lr.coef_*x.min(), lr.intercept_ + lr.coef_*x.max()]
plt.plot(x_values, y_values , marker = 'o', color='red')

# show the plot
plt.show()
