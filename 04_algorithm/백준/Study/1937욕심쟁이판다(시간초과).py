import sys
sys.stdin = open("1937.txt")

from collections import deque


n = int(input())

bamboo = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1, 1, 0, 0]

K = 0
def panda(x,y):
    global K
    visited[y][x] = 1
    q = deque()
    q. append([x,y])

    while q:
        t = q.popleft()
        x = t[0]
        y = t[1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny <n:
                if bamboo[ny][nx] > bamboo[y][x] :
                    if visited[ny][nx] <= visited[y][x] + 1:
                        visited[ny][nx] = visited[y][x] + 1
                        q.append([nx,ny])
                        if K < visited[ny][nx]:
                            K = visited[ny][nx]

visited = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == -1:
            panda(j,i)

print(K)