import sys

sys.stdin = open("2573.txt")

N,M = map(int, input().split())

sea = [list(map(int, input().split())) for _ in range(N)]


dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[0 for _ in range(M)] for _ in range(N)]
flag = 1


def bfs(x,y):
    visited[y][x] = 1
    q = []
    q.append([x,y])
    while q:
        t = q.pop(0)
        for k in range(4):
            nx = t[0] + dx[k]
            ny = t[1] + dy[k]
            if 0<= nx < M and 0<= ny <N and visited[ny][nx] == 0 and sea[ny][nx] > 0:
                visited[ny][nx] = 1
                q.append([nx,ny])

island = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and sea[i][j] > 0:
            bfs(j,i)
            island += 1
if island >= 2 :
    flag = 0

year = 0

while flag:
    visited = [[0 for _ in range(M)] for _ in range(N)]
    melt = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if sea[i][j] > 0:
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0<= nx < M and 0<= ny <N and sea[ny][nx] <= 0:
                        melt[i][j] += 1

    for i in range(N):
        for j in range(M):
            if sea[i][j] > 0:
                sea[i][j] -= melt[i][j]

    year += 1

    island = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and sea[i][j] > 0:
                bfs(j, i)
                island += 1

    if island >= 2:
        flag = 0
    elif island == 0:
        flag = 0
        year = 0

print(year)