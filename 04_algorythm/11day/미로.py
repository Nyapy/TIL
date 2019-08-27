import sys

sys.stdin = open('미로.txt')

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def ariadne(x,y):
    global cola
    if laby[y][x] == 3:
        cola =1

    if cola == 1:
        return
    check[y][x] = 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx >=0 and ny >= 0 and nx <N and ny <N:
            if check[ny][nx] == 0 and laby[ny][nx] != 1:
                ariadne(nx, ny)


for tc in range(T):
    N = int(input())
    cola = 0

    laby = [list(map(int, input())) for _ in range(N)]
    check = [[0 for __ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if laby[i][j] == 2:
                x = j
                y = i
                break

    ariadne(x, y)

    # print(laby)

    print('#{} {}' .format(tc+1, cola))