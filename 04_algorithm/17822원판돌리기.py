import sys

sys.stdin = open("17822.txt")

N,M,T = map(int, input().split())

circle = [[0]]+[list(map(int, input().split())) for _ in range(N)]

xdk = [list(map(int, input().split())) for _ in range(T)]

dist = [0]*(N+1)

dx = [0,1,0,-1]
dy = [-1,0,1,0]

all = 0
cnt = 0
for i in range(1,N+1):
    for j in range(M):
        all += circle[i][j]
        cnt += 1


for x,d,k in xdk:
    if cnt == 0:
        break
    for i in range(1,N+1):
       if i%x == 0:
           tem = [0] * M
           if d == 0:
               for j in range(M):
                   tem[j] = circle[i][(j - k + M) % M]
           elif d == 1:
               for j in range(M):
                   tem[j] = circle[i][(j + k) % M]
           circle[i] = tem

    visited = set()

    for i in range(1,N+1):
        for j in range(M):
            tx,ty = j,i
            if circle[ty][tx]:
                for w in range(4):
                    nx,ny = (tx+M+dx[w])%M, ty+dy[w]
                    if 1<=ny<N+1:
                        if circle[ty][tx] == circle[ny][nx]:
                            visited.add((nx,ny))

    if len(visited):
        for x,y in visited:
            all -= circle[y][x]
            cnt -= 1
            circle[y][x] = 0
    else:
        if cnt != 0:
            aver = all/cnt
            for i in range(1, N+1):
                for j in range(M):
                    if circle[i][j]:
                        if circle[i][j] > aver:
                            circle[i][j] -=1
                            all -= 1
                        elif circle[i][j] < aver:
                            circle[i][j] += 1
                            all += 1

print(all)