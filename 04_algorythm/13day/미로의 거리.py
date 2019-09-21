import sys

sys.stdin = open('미로의 거리.txt')

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def these(x, y):
    check[x][y] == 1

    queque.append([x,y])

    while queque:
        t = queque.pop()
        tx ,ty = t[0], t[1]
        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]
            if nx >= 0 and ny >= 0 and nx < N and ny <N :
                if check[nx][ny] == 0 and laby[nx][ny] != 1 :
                    queque.append([nx,ny])
                    check[nx][ny] = 1+check[tx][ty]
for tc in range(1,T+1):
    N = int(input())
    laby = [list(map(int, input())) for _ in range(N)]
    check = [[0 for _ in range(N)] for __ in range(N)]
    k = 0
    queque = []
    for i in range(N):
        for j in range(N):
            if laby[i][j] == 2:
                x = i
                y = j
                k = 1
                break
        if k == 1:
            break
    these(x, y)
    k= 0
    for i in range(N):
        for j in range(N):
            if laby[i][j] == 3:
                if check[i][j] != 0:
                    print('#{} {}' .format(tc, check[i][j]-1))
                    k = 1
                    break
                else :
                    print('#{} {}'.format(tc, check[i][j]))
        if k == 1:
            break