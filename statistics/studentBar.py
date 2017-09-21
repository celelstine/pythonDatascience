from matplotlib import pyplot as plt


friend_counts = Counter(num_friends) 
xs = range(10)
ys = [friend_counts[x] for x in xs] 
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()