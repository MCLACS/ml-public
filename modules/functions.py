import numpy as np

# converts a 1D python list to a
# to a NumPy 2D array with just one column
def listTo2DNumPy(l):
    a = []
    for n in l:
        a.append([n])
    return np.array(a)
