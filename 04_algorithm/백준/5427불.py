import sys

sys.stdin = open("5427불.txt")

from collections import deque

T = int(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def exit(x, y):
    global visited
    sec = 1
    visited[y][x] = sec

    tem_burn = bull
    tem_q = deque()
    tem_q.append([x,y])

    while sec :
        burn = tem_burn
        tem_burn = deque()

        while burn:
            t = burn.popleft()
            tx = t[0]
            ty = t[1]
            visited[ty][tx] = 1

            for k in range(4):
                nx = tx + dx[k]
                ny = ty + dy[k]
                if 0<= nx <w and 0 <= ny <h and building[ny][nx] =='.' and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    tem_burn.append([nx,ny])

        if tem_q:
            q = tem_q
            tem_q = deque()
        else:
            return "IMPOSSIBLE"

        while q:
            t = q.popleft()
            tx = t[0]
            ty = t[1]
            visited[ty][tx] = 1

            for k in range(4):
                nx = tx + dx[k]
                ny = ty + dy[k]
                if 0<= nx <w and 0 <= ny <h:
                    if building[ny][nx] == '.' and visited[ny][nx] == 0:
                        tem_q.append([nx,ny])
                        visited[ny][nx] = 1
                else:
                    return sec
        sec += 1



for tc in range(1, T + 1):
    w, h = map(int, input().split())

    building = [list(input()) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]

    bull = deque()

    for i in range(h):
        for j in range(w):
            if building[i][j] == "@":
                sx, sy = j, i
                building[i][j] = '.'

            elif building[i][j] == "*":
                bull.append([j,i])
                visited[i][j] = 1

    print(exit(sx,sy))