import sys

sys.stdin = open("2117.txt")

T = int(input())

for tc in range(1,1+T):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    