import sys

sys.stdin = open('암호코드스캔.txt')

T = int(input())

for tc in range(1,1+T):
    N,M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(M):
        for j in range(N):
            if arr[i][j] != 0: