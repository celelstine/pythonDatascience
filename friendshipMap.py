"""
  Function to display a map of friends of friends
"""
import itertools
def friendshipMap(friendshipList):
  people = set(itertools.chain.from_iterable(friendshipList))

  # get no of people in the map
  no_of_people = len(people)
  # create a default matrix of zero frames
  defaultFriendshipMap = [
    [0 for i in range(no_of_people)]
    for j in range(no_of_people)]
  # mark friendship spot
  for (a, b) in friendshipList:
    defaultFriendshipMap[a][b] = 1
    defaultFriendshipMap[b][a] = 1
  print list(people)
  for friend_zone in defaultFriendshipMap:
    print friend_zone

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
friendshipMap(friendships)
# friendshipMap([('esther', 'db'), ('db', 'mazi')])