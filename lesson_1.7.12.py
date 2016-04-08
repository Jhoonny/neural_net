import numpy as np
from numpy.linalg import linalg
"""
Beta = (X.T*X)**(-1)*X.T*Y

"""
y = np.array([[10],[7],[12]])

x = np.array([[1,60],[1,50],[1,75]])

print(y)
print(x)

b = ((linalg.inv(x.T.dot(x))).dot(x.T)).dot(y)
print(b)
