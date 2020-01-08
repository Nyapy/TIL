import sys

sys.stdin = open("5427불.txt")

from collections import deque

T = int(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y,f):
    visited[y][x] = 1
    q = deque()
    q.append([x,y])

    while q:
        t = q.popleft()
        tx = t[0]
        ty = t[1]

        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]

            if 0 <= nx < w and 0 <= ny < h:
                if building[ny][nx] == '.':
                    if visited[ny][nx] > visited[ty][tx] +1:
                        visited[ny][nx] = visited[ty][tx] +1
                        q.append([nx,ny])

            else:
                if f :
                    return visited[ty][tx]

    return "IMPOSSIBLE"

for tc in range(1, T + 1):
    w, h = map(int, input().split())

    building = [list(input()) for _ in range(h)]
    visited = [[99999999 for _ in range(w)] for _ in range(h)]
    fire = []
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                building[i][j] = '.'
                sx = j
                sy = i

            elif building[i][j] == "*":
                bfs(j,i,0)

    print(bfs(sx,sy,1))