# import the numpy library...
import numpy as np

# create a list of list using the built-in
# python list data structure...
listOfLists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
print("List of lists:\n%s\n" % listOfLists)

# convert the list of lists to a numpy matrix...
matrix = np.array(listOfLists)
print("NumPy matrix:\n%s\n" % matrix)

# turn it back into a list...
listAgain = matrix.tolist()
print("List Again:\n%s\n" % listAgain)

# methods that describe the matrix structure
a = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
b = np.array([ [1, 1, 1], [1, 1, 1], [2, 2, 2] ])

print("a = \n%s\n" % a)

print("Type: %s" % type(matrix))
print("Shape: %s" % str(matrix.shape))
print("Size: %d" % matrix.size)
print("Sum of all elements: %s" % a.sum())
print("Min of all elements: %s" % a.min())
print("Max of all elements: %s" % a.max())
print("Column sums of a: %s" % a.sum(axis=0))
print("Row sums of a: %s\n" % a.sum(axis=1))

# build a large matrix with default values...
matrix = np.arange(10000).reshape(100,100)
print("NumPy large matrix:\n%s\n" % matrix)

# matrix arithmetic
a = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
b = np.array([ [1, 1, 1], [1, 1, 1], [2, 2, 2] ])

print("a = \n%s\n" % a)
print("b = \n%s\n" % b)

c = a - b
print("a - b = \n%s\n" % c)

c = a*2
print("a*2 = \n%s\n" % c)

c = a**2
print("a**2 = \n%s\n" % c)

c = a/2
print("a/2 = \n%s\n" % c)

c = a>2
print("a>2 = \n%s\n" % c)

c = a*b
print("a*b = \n%s\n" % c)

# indexing
print("a = \n%s\n" % a)
print("a[2,0] = %s\n" % a[2,0])

print("a = \n%s\n" % a)

# slicing
print("a[0:3, 1] = %s\n" % a[0:3, 1])
print("a[:, 1] = %s\n" % a[:, 1])
print("a[2,0:3] = %s\n" % a[2,0:3])
print("a[2,:] = %s\n" % a[2,:])
print("a[0:2,0:3] = \n%s\n" % a[0:2,0:3])
print("a[0:2,:] = \n%s\n" % a[0:2,:])
print("a[0:2,1:3] = \n%s\n" % a[0:2,1:3])
