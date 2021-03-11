import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

X = np.loadtxt('GradePredictor.csv',skiprows=0, unpack=False, delimiter=',', encoding='utf-8-sig')
print(X)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)

x = []
for i in range(0, len(X[0:])):
	x.append(i)

plt.scatter(x, X[:,0])
plt.scatter(x, X[:,1])
plt.scatter(x, X[:,2])
plt.xlabel('Grade Predictor Features (unscaled)')
plt.ylabel('Data Point')
plt.title('Features (unscaled)')
plt.xlim(left=0)
plt.ylim(bottom=-100)
plt.ylim(top=1800)
plt.show()

plt.scatter(x, X_scaled[:,0])
plt.scatter(x, X_scaled[:,2])
plt.scatter(x, X_scaled[:,1])
plt.xlabel('Grade Predictor Features (scaled)')
plt.ylabel('Data Point')
plt.title('Features (scaled)')
plt.xlim(left=0)
plt.ylim(bottom=-5)
plt.ylim(top=5)
plt.show()
