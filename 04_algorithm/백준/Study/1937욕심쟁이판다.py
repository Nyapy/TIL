import sys
sys.stdin = open("1937.txt")

from collections import deque

n = int(input())

bamboo = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1, 1, 0, 0]

K = 1
mm = []
for i in range(n):
    for j in range(n):
        mm.append([bamboo[i][j],j,i])
mm.sort()

for a in range(n**2):
    x = mm[a][1]
    y = mm[a][2]

    if visited[y][x] == 0:
        visited[y][x] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < n and 0 <= ny < n :
                if bamboo[ny][nx] > bamboo[y][x]:
                    if visited[ny][nx] < visited[y][x]+1:
                        visited[ny][nx] = visited[y][x] + 1
                        if visited[ny][nx] > K:
                            K = visited[ny][nx]

    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < n and 0 <= ny < n :
                if bamboo[ny][nx] > bamboo[y][x]:
                    if visited[ny][nx] < visited[y][x]+1:
                        visited[ny][nx] = visited[y][x] + 1
                        if visited[ny][nx] > K:
                            K = visited[ny][nx]

print(K)