import numpy as np
import matplotlib.pyplot as plt

# create about 50 points betweeb 0 and 10
x = np.linspace(0, 10, 50)
# find the sin amd cos of the collection above
sinus = np.sin(x)
cosinus = np.cos(x)
#  plot a graph of number against sin and cos respectively

plt.plot(x, sinus, label='sinus', color='blue', linestyle='--', linewidth=2)
plt.plot(x, cosinus, label='cosinus', color='red', linestyle='-', linewidth=2)
plt.legend()
plt.show()


# plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()

# # plot series of graph
# # create a numpy series
# series1 = np.linspace(0, 10, 20)
# plt.plot(series1, series1, 'r-_', series1, series1**2, 'bs', series1, series1/2, 'g^', linewidth=4.0)
# plt.show()


# plot sub figure in a graph
# def f(t):
#   return np.exp(-t) * np.cos(2*np.pi*t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure(1)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()