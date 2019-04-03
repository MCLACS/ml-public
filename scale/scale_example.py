import numpy as np
from sklearn.preprocessing import MinMaxScaler 

X = np.array([[ 1., -1.,  2.], [ 2.,  0.,  0.], [ 0.,  1., -1.]])
scaler = MinMaxScaler() 
X_scaled = scaler.fit_transform(X) 
print(X_scaled)

