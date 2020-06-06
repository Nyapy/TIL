import sys

sys.stdin=open("17779.txt")

N = int(input())

city = [list(map(int, input().split())) for _ in range(N)]

print(city)

for i in range(N-2):
    for j in range(1,N-2):
        for k in range(1,min(j+1,N-1-i)):
            for l in range(1):
                1