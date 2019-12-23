import sys
sys.stdin = open("미세먼지.txt")
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
R, C, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
up, down = 0, 0
for y in range(R):
    if MAP[y][0] == -1:
        up = y
        down = y+1
        break
for _ in range(T):
    dust = [[0]*C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if MAP[y][x] > 4:
                buf = MAP[y][x] // 5
                for c in DIR:
                    Y = y+c[0]
                    X = x+c[1]
                    if 0 <= Y < R and 0 <= X < C:
                        if MAP[Y][X] == -1:
                            continue
                        dust[Y][X] += buf
                        MAP[y][x] -= buf
    for y in range(R):
        for x in range(C):
            MAP[y][x] += dust[y][x]
    for i in range(up-1, 0, -1):
        MAP[i][0] = MAP[i-1][0]
    del MAP[0][0]
    MAP[0].append(0)
    for i in range(up):
        MAP[i][C-1] = MAP[i+1][C-1]
    MAP[up].pop()
    MAP[up].insert(0, -1)
    MAP[up][1] = 0
    for i in range(down, R-1):
        MAP[i][0] = MAP[i+1][0]
    del MAP[R-1][0]
    MAP[R-1].append(0)
    for i in range(R-1, down, -1):
        MAP[i][C-1] = MAP[i-1][C-1]
    MAP[down].pop()
    MAP[down].insert(0, -1)
    MAP[down][1] = 0
res = 0
for y in range(R):
    for x in range(C):
        res += MAP[y][x]
print(res+2)