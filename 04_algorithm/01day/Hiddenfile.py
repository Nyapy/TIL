import numpy as np

c = range(3, 121, 3)
c = np.array(c)
ca = c.reshape(8,5)
print(ca)
cna = ca.reshape(4,10)
print(cna)