import sys

sys.stdin = open("17143.txt")

R,C,M = map(int, input().split())

sharks = [list(map(int, input().split())) for _ in range(M)]

ans = 0
print(sharks)
king = 0
while king < C:
    king += 1
