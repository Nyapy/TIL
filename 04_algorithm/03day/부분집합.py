import time
from time import strftime
start_time = time.time()






def printlist(data, bit):
    for i in range(len(bit)):
        if bit[i]:
            print(data[i], end = " ")
    print()


data = [1, 2, 3]
bit = [0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            printlist(data, bit)

print(time.time() - start_time, 'seconds')