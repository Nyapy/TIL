import sys

sys.stdin = open('미로1.txt')

T = 10

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def start():
    for i in range(16):
        for j in range(16):
             if laby[i][j] ==2:
                x = i
                y = j
                return x, y

def dsf(x,y):
    global cola

    if cola == 1:
        return
    check[x][y] = 1


    if laby[x][y] == 3 :
        cola = 1
        goal[0] = 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >=0 and ny >= 0 and nx < 16 and ny <16:
            if laby[nx][ny] != 1 and check[nx][ny] == 0:
                dsf(nx,ny)

for tc in range(T):
    cola = 0
    TC = input()

    laby = [list(map(int, input())) for _ in range(16)]
    check = [[0 for __ in range(16)] for _ in range(16)]
    goal = [0]


    dsf(start()[0], start()[0])

    print('#{} {} {}' .format(TC, cola, goal[0]))