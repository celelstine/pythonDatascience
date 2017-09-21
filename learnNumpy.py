from __future__ import print_function
import numpy as np

# NumPy is an extension to the Python programming language, adding support for large, 
# multi-dimensional (numerical) arrays and matrices, 
# along with a large library of high-level mathematical functions to operate on these arrays

# create an ndarrays from list and you have more powerful possiblities

list_of_numbers = [1,2,3,4,5,6,7,8,9]
nd_nums = np.array(list_of_numbers)
#  print awesome attributes
print('dimensions', nd_nums.ndim, 'shape', nd_nums.shape)

# create a two dimesional list
nd_2dim = np.array([range(1,5), range(5,9)])
print(nd_2dim, 'dimensions', nd_2dim.ndim, 'shape', nd_2dim.shape, 'size', nd_2dim.size)


print('A list of zeros', np.zeros(10))
print('Fill a matrix withzeros', np.zeros((3,6)))

print('A list of zeros', np.ones(10))
print('Fill a matrix withzeros', np.ones((3,6)))

print('create equal points (like 5 points) between two end points', np.linspace(0,1,5))
print('create equal log space between two end points', np.logspace(0,1,5))
 
print('reshape an array into a matrix', np.arange(10, dtype=float).reshape((2, 5)))


names = np.array(['Bob', 'Joe', 'Will', 'Bob'])
print('inline query ', names[names != 'Bob'])
# assign a vaue the query result --> names[names != 'Bob'] = 'Joe'
print(names)

# Compute Euclidean distance between 2 vectors
vec1 = np.random.randn(4)
vec2 = np.random.randn(4)
dist = np.sqrt(np.sum((vec1 - vec2) ** 2))
print(vec1, vec2, dist)