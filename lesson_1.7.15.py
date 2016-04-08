import urllib
from urllib import request
import numpy as np
from numpy.linalg import linalg

# fname = input()  # read file name from stdin
fname = "https://stepic.org/media/attachments/lesson/16462/boston_houses.csv"
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with
print(data.shape)
# input in web

# X0 = np.ones_like(data)
X = np.copy(data)
X[:, 0] = 1

Y = np.copy(data)[:,0]
Y = data[:,0]

# X = np.hstack((np.ones_like(Y), X0))

B = ((linalg.inv(X.T.dot(X))).dot(X.T)).dot(Y)

# print("".join(map(str,B)))
print(*B)

