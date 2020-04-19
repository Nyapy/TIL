import numpy as np

li = [ [1,2,3,4],
	[5,6,7,8],
[9,10,11,12]]

a = np.array(li)

res = a[[0,1,2],[2,3,2]]

print(res)


