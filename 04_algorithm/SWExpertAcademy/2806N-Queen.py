import sys

sys.stdin = open('2806.txt')

T = int(input())

def dfs(x,y, n):
    if col[x]: return
    if col[y]: return



for tc in range(1,T+1):
    N = int(input())

    board = [[0 for _ in range(N)] for _ in range(N)]
    col = [0] * N
    rum = [0] * N

    for i in range((N//2)+1):
        for j in range((N//2)+1):
            dfs(j,i)