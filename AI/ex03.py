import numpy as np

li = [ [1,2,3,4],
	[5,6,7,8],
[9,10,11,12]]


aa = np.array(li)

b_arr = np.array([[True, False, True, False],[True, False, True, False],[True, False, True, False]]
)
n = aa[b_arr]

print(b_arr)

print(n)

b_arr2 = (aa%2==0)

print(b_arr2)

n2 = aa[b_arr2]

print(n2)

n3 = aa[aa%2 == 0]

print(n3)