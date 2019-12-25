import sys
import copy

sys.stdin = open("1194달이차오른다.txt")

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N, M = map(int, input().split())

laby = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if laby[i][j] == "0":
            minsic = [j,i]
            laby[i][j] = "."

visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(64)]
print(list(map(ord, ["a", "f", "A", "F"])))

def bfs(x,y,d):
    visited[d][y][x] =1
    q = []
    q.append([x,y])

    while q:
        t = q.pop(0)
        for k in range(4):
            nx = t[0] + dx[k]
            ny = t[1] + dy[k]

            if 0<= nx <M and 0 <= ny <N and visited[d][ny][nx] == 0:
                if laby[ny][nx] == '.':
                    visited[d][ny][nx] = 1 + visited[d][t[1]][t[0]]
                    q.append([nx,ny])

                elif 97 <= ord(laby[ny][nx]) <= 102:
                    if ((ord(laby[ny][nx])-97) & d):
                        pass
                    else:
                        bfs(nx,ny,d+2**(ord(laby[ny][nx])-97))
                elif 65 <= ord(laby[ny][nx]) <= 70:
                    

