import sys

sys.stdin = open("10844.txt")

N = int(input())

result = 0
def stair(k,n):
    global result
    if k == N-1:
        result+=1
        return
    else:
        if n+1 < 10:
            stair(k+1, n+1)
        if n-1 >=0:
            stair(k+1, n-1)

for i in range(1,10):
    stair(0,i)

print(result%1000000000)