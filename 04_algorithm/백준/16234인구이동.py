import sys

sys.stdin = open("16234.txt")

N, L, R = map(int, input().split())

A = [0]+[[0]+list(map(int, input().split())) for _ in range(N)]


dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(y,x):
    check = 0
    population = A[y][x]
    q = []
    q.append([x,y])
    visited[y][x] = 1
    cnt = 1

    while q:
        t = q.pop(0)
        for k in range(4):
            nx = t[0] + dx[k]
            ny = t[1] + dy[k]
            if 1 <= nx < N+1 and 1 <= ny < N+1 and visited[ny][nx] == 0:
                if L<=  abs( A[ny][nx]-A[t[1]][t[0]] )<=R:
                    check = 1
                    visited[ny][nx] = 1
                    q.append([nx,ny])
                    population += A[ny][nx]
                    cnt += 1
                    tem.append([nx,ny])
    if check :
        tem.append([x,y])
        return population//cnt

    else:
        return 0

flag = 1
move = 0

while flag:
    visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    border = []
    ingoo = []
    for i in range(1,N+1):
        for j in range(1,N+1):

            if visited[i][j] ==0:
                tem = []
                man = bfs(i,j)
                if man :
                    border.append(tem)
                    ingoo.append(man)

    if border and ingoo:
        for a in range(len(border)):
            for b in range(len(border[a])):
                A[border[a][b][1]][border[a][b][0]] = ingoo[a]
        move += 1

    else:
        flag = 0


print(move)

