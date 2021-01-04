import numpy as np
import matplotlib.pyplot as plt

# CRICK-X.csv
# Columns: Chirp Freq
# CRICK-Y.csv
# Columns: Temp F
x = np.loadtxt('CRICK-X.csv',skiprows=1, unpack=False, delimiter=',')
y = np.loadtxt('CRICK-Y.csv',skiprows=1, unpack=False, delimiter=',')

print('x-values shape: %s' % str(x.shape))
print('y-values shape: %s' % str(y.shape))
print('First 5 x-values: %s' % x[:5])
print('First 5 y-values %s' % y[:5])

plt.scatter(x, y)
plt.xlabel('chirp freq')
plt.ylabel('temp')
plt.title('Crickets Regression')
plt.show()
