import sys

sys.stdin = open("1012.txt")
from collections import deque
T = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y) :
    farm[y][x] = 1
    q = deque()
    q.append([x,y])

    while q:
        t = q.popleft()
        x = t[0]
        y = t[1]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx <M and 0 <= ny < N:
                if farm[ny][nx] == -1:
                    farm[ny][nx] =1
                    q.append([nx,ny])

for tc in range(1,1+T):
    M, N, K = map(int, input().split())

    farm = [[0]*M for _ in range(N)]

    result = 0
    for i in range(K):
        x, y = map(int, input().split())
        farm[y][x] = -1

    for i in range(N):
        for j in range(M):
            if farm[i][j] == -1:
                result += 1
                bfs(j,i)

    print(result)