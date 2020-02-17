import sys

sys.stdin = open("13458.txt")

N = int(input())

place = list(map(int, input().split()))

B,C = map(int, input().split())

result = N

for i in range(N):
    place[i] -= B
    if place[i] > 0:
        if place[i]%C == 0:
            result += place[i]//C
        else:
            result += (place[i]//C)+1
print(result)