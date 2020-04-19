import numpy as np

a = np.array([[1,2],[3,4]])

s = np.sum(a)

print(s)

s = np.sum(a, axis = 0)

print(s)

s = np.sum(a, axis=1)

print(s)