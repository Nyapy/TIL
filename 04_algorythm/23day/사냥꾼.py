import sys

sys.stdin = open('사냥꾼.txt')

T = int(input())
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1 ,1, 1, 0, -1]
def hunt(i,j):
    global rabbit

    for k in range(8):
        nx = j
        ny = i
        while 1:
            nx = nx + dx[k]
            ny = ny + dy[k]
            if nx >= 0 and ny >= 0 and nx < N and ny < N:
                if field[ny][nx] == 2:
                    rabbit +=1
                elif field[ny][nx] ==3:
                    break

            else:
                break



for tc in range(1,1+T):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0 for _ in range(N)] for __ in range(N)]
    # print(field)
    rabbit = 0

    for i in range(N):
        for j in range(N):
            if field[i][j] == 1:
                hunt(i,j)

    print('#{} {}' .format(tc, rabbit))