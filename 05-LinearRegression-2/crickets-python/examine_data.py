import numpy as np
import matplotlib.pyplot as plt

all = np.loadtxt('CRICK.csv',skiprows=1, unpack=False, delimiter=',')

# slice so x is the first column and y is the second column
x = all[:, 0]
y = all[:, 1]

# take a look at the data...
print('x shape: %s' % str(x.shape))
print('y shape: %s' % str(y.shape))
print('x min/max= %.2f/%.2f' % (x.min(), x.max()))
print('y min/max= %.2f/%.2f' % (y.min(), y.max()))
print('first five rows x= \n%s' % x[0:5])
print('first five rows y= \n%s' % y[0:5])

# plot the data...
plt.scatter(x, y)
plt.xlabel('Chirp Freq')
plt.ylabel('Temp')
plt.title('Crickets Chirp vs. Temp')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.show()
