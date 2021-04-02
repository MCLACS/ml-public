#################################################
# Try first as is...
# Next add a second hidden layer
# Finally scale it
#################################################
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

train = np.loadtxt('handwriting.csv',skiprows=1, unpack=False, delimiter=',')

y = train[:, 0]
X = train[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state = 12)

# summarize data...
print('X train shape: %s' % str(X_train.shape))
print('y train shape: %s' % str(y_train.shape))
print('x train min/max= %.2f/%.2f' % (X_train.min(), X_train.max()))
print('y train min/max= %.2f/%.2f' % (y_train.min(), y_train.max()))
print('first five rows of X train= \n%s' % X_train[0:6, :])
print('first 150 rows of y train= \n%s' % y_train[0:150])

plt.matshow(X_train[3].reshape(28,28))
plt.show()
