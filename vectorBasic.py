def make_matrix(num_rows, num_cols, entry_fn):
  """returns a num_rows x num_cols matrix
  whose (i,j)th entry is entry_fn(i, j)"""
  return [
    [entry_fn(i, j) for j in range(num_cols)] 
    for i in range(num_rows)]

def is_diagonal(i, j):
  """1's on the 'diagonal', 0's everywhere else"""
  return 1 if i==j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)
for i in identity_matrix:
  print i

#def friendsArray(friendHistory):
  # find the 
friendshipMatrix = [
    [(1 if i==j else 0) for j in range(5)] 
    for i in range(5)]

print friendshipMatrix