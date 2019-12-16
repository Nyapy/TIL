N,M = map(int, input().split())

office = [list(map(int, input().split())) for _ in range(N)]
check = [[10 for _ in range(M)] for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
min_cnt = 987654321
detector = []

for i in range(N):
    for j in range(M):
        if  1 <= office[i][j] <=5 :
            detector += [[j,i, office[i][j]]]

        if office[i][j] != 0 :
            check[i][j] = 0
direction = [[0] for _ in range(len(detector))]

def cameracheck(j,i, cnum, direction, now):
    if cnum == 1:
        directions = [direction]
    elif cnum == 2:
        directions = [direction, (direction+2)%4]
    elif cnum == 3:
        directions = [direction, (direction+1)%4]
    elif cnum == 4:
        directions = [direction, (direction+1)%4, (direction+2)%4]
    elif cnum == 5:
        directions = [0,1,2,3]

    for k in directions:
        x, y = j, i
        nx = x +dx[k]
        ny = y +dy[k]
        while nx >= 0 and ny >= 0 and nx < M and ny < N:
            if office[ny][nx] == 6:
                break
            else:
                now[ny][nx] = 0
                nx += dx[k]
                ny += dy[k]


def overlap(k):
    if k == len(direction):
        gamsi()
    else:
        for s in range(4):
            direction[k] = s
            overlap(k+1)

def gamsi():
    global min_cnt
    now = [[10 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if office[i][j] != 0:
                now[i][j] = 0
    cnt = 0
    for seq in range(len(detector)):
        cameracheck(detector[seq][0], detector[seq][1], detector[seq][2],direction[seq], now)

    for i in range(N):
        for j in range(M):
            if now[i][j] == 10:
                cnt += 1

    if min_cnt > cnt :
        min_cnt = cnt

overlap(0)

print(min_cnt)