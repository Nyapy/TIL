import sys

sys.stdin = open('미로2.txt')

T = 10
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def star(laby):
    for i in range(len(laby)):
        for j in range(len(laby[i])):
            if laby[i][j] == 2:
                x = i
                y = j
                return x,y

def tethe(a, b):
    check[a][b] = 1
    Q.append([a, b])

    while Q :
        t = Q.pop(0)

        for k in range(4):
            nx = t[0] + dx[k]
            ny = t[1] + dy[k]
            if nx >= 0 and ny >= 0 and nx < 100 and ny < 100:
                if check[nx][ny] == 0 and laby[nx][ny] != 1 :
                    check[nx][ny] = 1
                    Q.append([nx, ny])
                    if laby[nx][ny] == 3:
                        return

def solve(laby):
    for i in range(100):
        for j in range(100):
            if laby[i][j] == 3:
                print('#{} {}' .format(tc, check[i][j]))
                return

for tc in range(1,T+1):
    Tc = int(input())
    laby = [list(map(int, input())) for _ in range(100)]
    check = [[0 for _ in range(100)]for __ in range(100)]
    Q = []

    start = star(laby)

    tethe(start[0], start[1])

    solve(laby)
