import numpy as np
import matplotlib.pyplot as plt

# CRICK-X.csv
# Columns: Chirp Freq
# CRICK-Y.csv
# Columns: Temp F
x = np.loadtxt('CRICK-X.csv',skiprows=1, unpack=False, delimiter=',')
y = np.loadtxt('CRICK-Y.csv',skiprows=1, unpack=False, delimiter=',')

print('x shape: %s' % str(x.shape))
print('y shape: %s' % str(y.shape))
print('x min/max= %.2f/%.2f' % (x.min(), x.max()))
print('y min/max= %.2f/%.2f' % (y.min(), y.max()))
print('x= \n%s' % x)
print('y= \n%s' % y)

plt.scatter(x, y)
plt.xlabel('Chirp Freq')
plt.ylabel('Temp')
plt.title('Crickets Chirp vs. Temp')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.show()
