def dfs(v, id):
    visit[v] =  id
    for i in range(1, N+1):
        if G[v][i] and not visit[i]:
            dfs(i, id)

import sys
sys.stdin = open("(7465)창용마을무리의개수_input.txt")

T = int(input())
for tc in range(T):
    N,M = map(int, input().split())
    G = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visit = [0] * (N+1)
    cnt = 0

    for i in range(M):
        x, y = map(int, input().split())
        G[x][y] = G[y][x] = 1

    for i in range(1, N+1):
        if(visit[i]== 0):
            cnt += 1
            dfs(i, cnt)

    print("#{} {}".format(tc+1, cnt))