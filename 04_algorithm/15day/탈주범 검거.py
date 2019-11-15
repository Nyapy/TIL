import sys

sys.stdin = open('탈주범 검거.txt')

T = int(input())

def type0(x,y):
    global nx, ny, time
    if under[x][y] ==1:
        type1(x,y)
    if under[x][y] ==2:
        type2(x,y)
    if under[x][y] ==3:
        type3(x,y)
    if under[x][y] ==4:
        type4(x,y)
    if under[x][y] ==5:
        type5(x,y)
    if under[x][y] ==6:
        type6(x,y)
    if under[x][y] ==7:
        type7(x,y)


def type1(x,y):
    global nx, ny
    dx = [0, -1, 1, 0, 0]  # 정지, 좌,우, 하, 상
    dy = [0, 0, 0, 1, -1]
    for k in range(5):
        nx = x + dx[k]
        ny = y + dy[k]

def type2(x,y):
    global nx, ny
    dx = [0, 0, 0]  # 정지,상,하
    dy = [0, 1, -1]
    for k in range(3):
        nx = x+ dx[k]
        ny = y + dy[k]

def type3(x,y):
    global nx, ny
    dx = [0, -1, 1]  # 정지, 좌,우
    dy = [0, 0, 0]
    for k in range(3):
        nx = x+ dx[k]
        ny = y + dy[k]

def type4(x,y):
    global nx, ny
    dx = [0,  1, 0]  # 정지, 우, 상
    dy = [0,  0, -1]
    for k in range(3):
        nx = x+ dx[k]
        ny = y + dy[k]
def type5(x,y):
    global nx, ny
    dx = [0, 1, 0]  # 정지,우,하
    dy = [0, 0, 1]
    for k in range(3):
        nx = x+ dx[k]
        ny = y + dy[k]
def type6(x,y):
    global nx, ny
    dx = [0, -1, 0]  # 정지, 좌, 하
    dy = [0, 0, 1]
    for k in range(3):
        nx = x+ dx[k]
        ny = y + dy[k]
def type7(x,y):
    global nx, ny
    dx = [0, -1, 0]  # 정지, 좌, 상
    dy = [0, 0, -1]
    for k in range(3):
        nx = x+ dx[k]
        ny = y + dy[k]


def trace(x,y):
    global time
    time =0
    check[x][y] = 8
    q.append([x,y])
    while time <L:
        t= q.pop(0)
        type0(t[0],t[1])
        if nx >= 0 and ny >= 0 and nx <M and ny < N:
            if under[nx][ny] != 0 :
                check[nx][ny] = 8
                q.append(nx,ny)
                time += 1



for tc in range(1,1+T):
    N,M,R,C,L = map(int, input().split())
    under = [list(map(int, input().split())) for _ in range(N)]
    check = [[0 for _ in range(M)] for __ in range(N)]
    q = []
    # print(under)
    # print(check)
    trace(R,C)
    cnt = 0

    for i in range(M):
        for j in range(N):
            if check[i][j] == 8:
                cnt +=1


    print('#{} {}' .format(tc, cnt))