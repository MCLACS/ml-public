#################################################
# Try first as is...
# Next add a second hidden layer
# Finally scale it
#################################################
import pandas as pd
import numpy as np

# load all names...
names = []
skip = True
f = open("zomato_names.csv", "r")
for line in f:
	if skip == False:
		names.append(line.rstrip());
	skip = False
print('Name count: %s' % str(len(names)))
print('First five names= \n%s' % names[0:5])
f.close()

# look at the first row to get the features...
f = open("zomato.csv", "r")
features = f.readline();
print('Features: \n%s' % features)
f.close()

# using read_csv here because load text was giving me trouble...
data = pd.read_csv('zomato.csv')
data = data.to_numpy()

# summarize data...
print('Shape of data: %s' % str(data.shape))
print('First five rows of data= \n%s' % data[0:6, :])
