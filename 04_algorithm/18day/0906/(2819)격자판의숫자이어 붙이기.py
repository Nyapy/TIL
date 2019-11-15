def dfs(x, y, k, n):
    global cnt
    if k == 7:
        if visit[n] != tc:
            cnt += 1
            visit[n] = tc
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 4 or ny < 0 or ny >=  4: continue
        dfs(nx, ny, k + 1, n * 10 + data[nx][ny])

import sys
sys.stdin = open("(2819)격자판의숫자이어 붙이기_input.txt")
T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [0] * 10000000

for tc in range(1, T+1):
    data = [[0 for _ in range(4)] for _ in range(4)]
    cnt = 0
    for i in range(4):
        data[i] = list(map(int, input().split()))

    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, data[i][j])

    print("#{} {}".format(tc, cnt))