import sys

sys.stdin = open("hiking.txt")

T = int(input())


def hike(j, i, k, d):
    global longest
    if longest < d:
        longest = d
    visited[i][j] = 1

    x = j
    y = i
    for e in range(4):
        nx = x + dx[e]
        ny = y + dy[e]
        if nx >= 0 and ny >= 0 and nx < N and ny < N:
            if visited[ny][nx] == 0:
                if G[ny][nx] < G[y][x]:
                    hike(nx,ny, k, d+1)

                elif G[ny][nx]-G[y][x] < K and k == 0:
                    p = G[ny][nx]-G[y][x]
                    G[ny][nx] = G[y][x]-1
                    hike(nx, ny, 1, d+1)
                    G[ny][nx] = G[y][x]+p

    visited[i][j] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    G = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N) ]
    longest = 0

    m = 0
    highest = []
    for i in range(N):
        for j in range(N):
            if G[i][j] > m :
                m = G[i][j]

    for i in range(N):
        for j in range(N):
            if G[i][j] == m:
                q = []
                highest += [[j,i]]

    for a in range(len(highest)):
        hike(highest[a][0], highest[a][1], 0, 1)

    print("#{} {}" .format(tc, longest))