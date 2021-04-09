import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

data = pd.read_csv('zomato.csv')
data = data.to_numpy()

clusters = 10
kmeans = KMeans(n_clusters = clusters, random_state = 12)
kmeans.fit(data)
for x in range(0,clusters):
	print(np.count_nonzero(kmeans.labels_ == x))
print('first 100 labels/clusters = \n%s' % kmeans.labels_[0:100])

# get favorite name, convert to its index, get its cluster...

# if name is valid, look for another restaurant in the
# same cluster, then lookup that restaurant name and
# suggest it to the user...

# BONUS: pick the nth restaurant in the cluster where n is a random number
# from 1 to (1 - the number of restaurants in the cluster),
# this will add some variety to the suggestions
