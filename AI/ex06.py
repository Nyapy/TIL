import numpy as np

x = np.float32(1.0)

print(x)

print(type(x))

print(x.dtype)

z= np.arange(5)

print(z)

aa = np.array([1,2,3], dtype ='f')

print(aa)
print(aa.dtype)

xx = np.int8(aa)
print(xx)
print(xx.dtype)

b= np.arange(10)
bb = np.arange(3,10)

print(b)
print(bb)

c = np.arange(5, dtype=np.float)
cc = np.arange(5, dtype=np.float16)

print(c.dtype)
print(cc.dtype)

d = np.arange(2,3,0.2)

print(d)
