# ------------------------------------------------------
# This file is used to explore the structure and values
# of the sample iris datafile included with sklearn
# ------------------------------------------------------
import sys
sys.path.append('/home/ubuntu/workspace/utils')

import mglearn as mglearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 


X = np.loadtxt('Admission_Predict_NoLabels.csv',skiprows=1, unpack=False, delimiter=',')

kmeans = KMeans(n_clusters = 3) 
kmeans.fit(X) 
print(kmeans.labels_)
print(np.count_nonzero(kmeans.labels_ == 0))
print(np.count_nonzero(kmeans.labels_ == 1))
print(np.count_nonzero(kmeans.labels_ == 2))

