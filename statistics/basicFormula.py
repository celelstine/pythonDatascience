from __future__ import division
import math
# calculate the mean of a  dataset which is division of the sum by the number of items
# the mean express the density of the collection
def mean(x):
  return sum(x) / len(x)

# median : is the middle item , which express the center of a collection
def median(v):
  """finds the 'middle-most' value of v""" 
  n = len(v)
  sorted_v = sorted(v)
  # we use // to get an integer
  midpoint = n // 2
  # if we have just a single element then it is the median 
  if n == 1:
    return sorted_v[0]
  if n % 2 == 1:
    # if odd, return the middle value 
    return sorted_v[midpoint]
  else:
    # if even, return the average of the middle values 
    lo = midpoint - 1
    hi = midpoint
    sumOfMidTie = sorted_v[lo] + sorted_v[hi]
    return  sumOfMidTie / 2

# quantile: is the partial center of a collection, usually between 0-1
def quantile(x, p):
  """returns the pth-percentile value in x""" 
  p_index = int(p * len(x))
  return sorted(x)[p_index] # example quantile(students, 0.25)

def mode(x):
  """returns a list, might be more than one mode""" 
  counts = Counter(x)
  max_count = max(counts.values())
  return [x_i for x_i, count in counts.iteritems()
    if count == max_count]

# the range is used to loose  measure how spread the dataset is, it is the difference between the largest and smallest item
def data_range(x):
  return max(x) - min(x)

# a more precise method to measure the dispersion of data are:

# we substract the mean from every item in the collection
def de_mean(x):
  """translate x by subtracting its mean (so the result has mean 0)""" 
  x_bar = mean(x)
  return [x_i - x_bar for x_i in x]

# get the sum of the square of each item
def sum_of_squares(collection_of_items):
  sum_of_squares = 0
  if len(collection_of_items) < 1 :
    return 0
  for item in collection_of_items:
    sum_of_squares += item ** 2
  return sum_of_squares
# the variance is a ore precise measure of the dispersion
def variance(x):
  """assumes x has at least two elements""" 
  n = len(x)
  deviations = de_mean(x)
  return sum_of_squares(deviations) / (n - 1)

# since the variance is a mesure of the square of the items, 
# we can derive the actually dispersion by returning the square root of the variance
def standard_deviation(x): 
  return math.sqrt(variance(x))

# since the mean and variance has a limitation of reflecting change of a single item not the whole
#  a more robust commutation is the different between the two extreme middle quantile
def interquartile_range(x):
  return quantile(x, 0.75) - quantile(x, 0.25)

# Correlation : is the measure of the relationship between two dataset

# the dot function sums up the products of corresponding pairs of elements
def dot(collection1, collection2):
  sum_of_product = 0
  size_of_collection1 = len(collection1)
  index_counter = 0;
  while index_counter < size_of_collection1:
    sum_of_product += (collection1[index_counter] * collection2[index_counter])
    index_counter += 1
  return sum_of_product

# covariance is the measure of the sum dispersion
# when it is positive is shows direct proportionality
# when it is nevagive is show indirect proportionality,
# when it is zero is implies that there is no relationship 
def covariance(x, y): 
  n = len(x)
  return dot(de_mean(x), de_mean(y)) / (n - 1)

# a better measure is the division of the covariance by the standard deviation of the datasets
# The correlation is unitless and always lies between -1 (perfect anti-correlation) and 1 (perfect correlation)
def correlation(x, y):
  stdev_x = standard_deviation(x) 
  stdev_y = standard_deviation(y)
  if stdev_x > 0 and stdev_y > 0:
    return covariance(x, y) / stdev_x / stdev_y 
  else:
    return 0 # if no variation, correlation is zero

x=[-2,-1,0,1,2] 
y=[2, 1,0,1,2]

x1=[-2,1,0,1,2]
y1 = [99.98, 99.99, 100, 100.01, 100.02]
test_correlation1 = correlation(x,y)
test_correlation2 = correlation(x1,y1)
print(dot(x,y))
print test_correlation1, test_correlation2