def dfs(s):
    global flag
    visited[s] = 1

    if s == GOAL :
        flag = 1
        return

    for i in range(0, SIZE):
        if adj[s][i] == 1 and visited[i] == 0:
            dfs(i)

import sys
sys.stdin = open("(1219)길찾기_input.txt")
T = 10
SIZE = 100
GOAL = 99
for t in range(1, T+1):
    flag = 0
    no, length = map(int, input().split())
    temp = list(map(int, input().split()))
    adj = [[0 for i in range(SIZE)] for j in range(SIZE)]   # 2차원 초기화
    visited = [0 for i in range(SIZE)]                     # 방문처리

    for i in range(0, len(temp), 2):
        adj[temp[i]][temp[i+1]] = 1

    dfs(0)

    print("#{} {}".format(t, flag))