# python default division method returns integer, so use the import below
from __future__ import division
print (5/2)

def double(x):
  """this is where you put an optional docstring
  that explains what the function does.
  for example, this function multiplies its input by 2"""
  return x*2

def apply_to_one(f):
  """calls the function f with 1 as its argument"""
  return f(1)

# function can be assign to an object
my_double = double # refers to the previously defined function
x = apply_to_one(my_double) # equals 2

# use lambda express
y = apply_to_one(lambda x: x + 4)

# optional parameter
def subtract(a=0, b=0):
  answer = a-b
  # print answer
  return answer
subtract(10, 5) # returns 5
subtract(0, 5) # returns -5
subtract(b=5) # same as previous

# string 
tab_string = "\t"
# espace speacial characters with the raw operator
not_tab_string = r"\t" # represents the characters '\' and 't'
len(not_tab_string)
print 'knknksnks', '\n', 'fknkdk'
multi_line_string = """This is the first line.
    and this is the second line
    and this is the third line"""

# exception
try:
  print 0/0
except ZeroDivisionError:
  print "cannot divide by zero"

# list collections
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]
list_length = len(integer_list) # equals 3 list_sum = sum(integer_list) # equals 6

x = range(10) # is the list [0, 1, ..., 9]
nine = x[-1] # equals 9, 'Pythonic' for last element
eight = x[-2] # equals 8, 'Pythonic' for next-to-last element
x[0] = -1 # now x is [-1, 1, 2, 3, ..., 9]

first_three =x[:3] # [-1, 1, 2]
three_to_end = x[3:] # [3, 4, ..., 9]
one_to_four = x[1:5] # [1, 2, 3, 4]
last_three = x[-3:] # [7, 8, 9]
without_first_and_last = x[1:-1] # [1, 2, ..., 8]
copy_of_x = x[:] # [-1, 1, 2, ..., 9]

1 in [1, 2, 3] # True
0 in [1, 2, 3] # False

x, y = [1, 2] # now x is 1, y is 2

# tuple - immutable list 
my_tuple = (1, 2)
try:
  my_tuple[1] = 3
except TypeError:
  print "cannot modify a tuple"

# Tuples are a convenient way to return multiple values from functions:
def sum_and_product(x, y):
  return (x + y),(x * y), (x-y), (x/y)
arithmetics = sum_and_product(2, 3) # equals (5, 6)
print arithmetics
add,times, minus, divide  = sum_and_product(5, 10) # s is 15, p is 50
print add,times, minus, divide

# dictionaries
empty_dict = {} # Pythonic
empty_dict2 = dict() # less Pythonic
grades = { "Joel" : 80, "Tim" : 95 } # dictionary literal
# dictionary throws an error for keys not found
try:
  kates_grade = grades["Kate"]
except KeyError:
  print "no grade for Kate!"

# check if key exist
joel_has_grade = "Joel" in grades # True
kate_has_grade = "Kate" in grades # False

# to avoid error for unknown key , use the get operator
joels_grade = grades.get("Joel", 0) # equals 80
kates_grade = grades.get("Kate", 0) # equals 0
no_ones_grade = grades.get("No One") # default default is None

tweet = {
  "user" : "joelgrus",
  "text" : "Data Science is Awesome",
  "retweet_count" : 100,
  "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}
tweet_keys =tweet.keys() # ['text', 'retweet_count', 'hashtags', 'user']
tweet_values = tweet.values()
tweet_items = tweet.items()
print tweet_keys, tweet_values, tweet_items

# using default dictionary to handle key not found
# when a key does not exist , the default value of the datatype is used
from collections import defaultdict
word_counts = defaultdict(int) # int() produces 0
document = ['hello', 'people','mac os is sweet to use', 'hello desktop',  'people']
for word in document:
  word_counts[word] += 1
# this would throw an error , dd_list = {}
dd_list =  defaultdict(list)
dd_list[2].append(1)

# dict() produces an empty dict, # { "Joel" : { "City" : Seattle"}}
dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seattle"

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1 # now dd_pair contains {2: [0,1]}

# counter - are used to convert list of input into a key-value dictionary
from collections import Counter

c = Counter([0, 1, 2, 0]) # c is (basically) { 0 : 2, 1 : 1, 2 : 1 }
word_counts = Counter(document)
# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
  print word, count

# set - contains a list of distinct elements
# We'll use sets for two main reasons.
# The first is that in is a very fast operation on sets.
# If we have a large collection of items that we want to use for a membership test,
# a set is more appropriate than a list:
s = set()
s.add(1) # s is now { 1 }
s.add(2) # s is now { 1, 2 }
s.add(2) # s is still { 1, 2 }
x = len(s) # equals 2
y=2 in s # equals Truex
z=3 in s # equals False

# set can be used to collect distint elements from a set
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list) # 6
item_set = set(item_list) # {1, 2, 3}
num_distinct_items = len(item_set) # 3
distinct_item_list = list(item_set) # [1, 2, 3]

# Control Flow
# ternary if-then-else
parity = "even" if x % 3 == 0 else "odd" # pass-condition-fail
print parity

# break statement jumps the entire block while continue jumps to the next iteration
for x in range(10):
  if x == 3:
    continue # go immediately to the next iteration
  if x == 5:
    break # quit the loop entirely print x

# Truthiness

x = None
print x == None # prints True, but is not Pythonic
print x is None # prints True, and is Pythonic

# the following values return false: None, [], {}, set(), 0, 0.0
def some_function_that_returns_a_string():
  return 'cele loved God'
s = some_function_that_returns_a_string()
if s:
  first_char = s[0]
else:
  first_char = ""
# A simpler way of doing the same is:
first_char = s and s[0]
print first_char

# the all operator returns true when all values are true
all([True, 1, { 3 }]) # True
all([True, 1, {}]) # False, {} is falsy

# sorting
x = [4,1,2,3]
y = sorted(x) # is [1,2,3,4], x is unchanged
x.sort() # now x is [1,2,3,4]

# sort the list by absolute value from largest to smallest
x = sorted([-4,1,-2,3], key=abs, reverse=True) # is [-4,3,-2,1]
# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(),
  key=lambda (word, count): count,
  reverse=True)

# list comprehension examples
even_numbers = [x for x in range(5) if x % 2 == 0] # [0, 2, 4]
squares = [x * x for x in range(5)] # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers] # [0, 4, 16]

# You can similarly turn lists into dictionaries or sets:
square_dict = { x : x * x for x in range(5) } # { 0:0, 1:1, 2:4, 3:9, 4:16 }
square_set = { x * x for x in [1, -1] } # { 1 }

# If you don't need the value from the list,
# it's conventional to use an underscore as the variable:
zeroes = [0 for _ in even_numbers] # has the same length as even_numbers
# A list comprehension can include multiple fors:
pairs = [(x, y)
  for x in range(10)
  for y in range(10)] # 100 pairs (0,0) (0,1) ... (9,8), (9,9)
  # later fors can use the results of earlier ones:

# zip and Argument Unpacking
# - zip is use to map a list with another 
list1 = ['a', 'b', 'c', 'e']
list2 = [1, 2, 3, 4]
list3 = zip(list1, list2)
t = ('a','v', 1, 2)
u = ('b','x', 2, 3)
v = ('c','y', 3, 5)
x = ('d','z', 4)
print zip(t, u, v, list1)