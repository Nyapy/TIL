import numpy as np

a= np.array([[1,2],[3,4],[5,6]])
b = 10

c = a*b

print(c)

b = np.array([10,20])

c = a*b

print(c)

x = a.flatten()

print(a)

print(x[np.array([1,3,5])])

print(x[x>3])

print(x>3)