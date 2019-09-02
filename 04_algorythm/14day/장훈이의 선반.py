import time
from time import strftime
start_time = time.time()


import sys

sys.stdin = open('장훈이의 선반.txt')

T = int(input())

for tc in range(1, T+1):


    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    mind = B

    for i in range(1<<N):
        hap = 0
        for j in range(N) :
            if i &(1<<j) :
                hap += height[j]

        if hap >= B:
            dif = hap - B
            if mind > dif:
                mind = dif

    print('#{} {}' .format(tc, mind))


print(time.time() - start_time, 'seconds')