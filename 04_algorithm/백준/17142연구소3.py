import sys

sys.stdin= open("17142.txt")

from copy import deepcopy
from collections import deque
N,M = map(int, input().split())

dx = [0,1,0,-1]
dy = [-1,0,1,0]
lab = [list(map(int, input().split())) for _ in range(N)]
ans = N**2
# print(N,M)
# print(lab)

virus = []

hall = 0
for i in range(N):
    for j in range(N):
        if lab[i][j] ==2:
            virus.append([j,i])

        elif lab[i][j] == 0:
            hall += 1

active = [0] * len(virus)

def bfs(avir):
    colab = deepcopy(lab)
    cnt = 0
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque()
    for x,y in avir:
        visited[y][x] = 0
        q.append([x,y])

    while q:
        tx, ty = q.popleft()

        for k in range(4):
            nx, ny = tx+dx[k], ty +dy[k]

            if 0<=nx<N and 0<=ny<N:
                if visited[ny][nx] == -1 :
                    if colab[ny][nx] == 0:
                        visited[ny][nx] = visited[ty][tx] +1
                        cnt += 1
                        q.append([nx,ny])

                    elif colab[ny][nx] == 2:
                        visited[ny][nx] = visited[ty][tx] +1
                        q.append([nx,ny])

                    time = visited[ny][nx]

                    if cnt == hall:
                        return time
    return N**2




def powerset(n, k, q):
    global ans
    if hall==0:
        ans =0
        return
    if n-k < M-q:
        return
    if q == M:
        avir =[]
        for a in range(len(active)):
            if active[a]:
                avir.append(virus[a])
        check = bfs(avir)
        if ans > check:
            ans = check
        return

    else:
        active[k] =1
        powerset(n,k+1, q+1)
        active[k] =0
        powerset(n,k+1,q)

powerset(len(virus), 0,0)

if ans == N**2:
    print(-1)
else: print(ans)