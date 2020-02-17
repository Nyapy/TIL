import sys

sys.stdin = open("2151.txt")

from collections import deque

N = int(input())

house = [list(input()) for _ in range(N)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

doors = []

do = 0
for i in range(N):
    for j in range(N):
        if house[i][j] == '#':
            doors.append([j,i])

def search(x,y):
    q = deque()
    for k in range(4):
        q.append([x,y,k,0])
    while q:
        t = q.popleft()
        x =t[0]
        y =t[1]
        d =t[2]
        cnt = t[3]
        a =1
        while a:
            nx = x +dx[d]
            ny = y +dy[d]
            if 0 <= nx <N and 0 <= ny <N and house[ny][nx] != '*':
                x= nx
                y = ny
                if house[ny][nx] == '!':
                    q.append([nx, ny, (d + 1) % 4, cnt + 1])
                    q.append([nx, ny, (d + 3) % 4, cnt + 1])
                elif nx == doors[1][0] and ny == doors[1][1]:
                    return cnt
            else:
                a =0
    return 0

print(search(doors[0][0], doors[0][1]))