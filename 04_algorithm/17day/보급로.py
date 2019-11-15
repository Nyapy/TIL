import sys

sys.stdin = open('보급로.txt')

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def short(x,y):
    time[y][x] += ground[y][x]
    check[y][x] = 1
    q.append([x,y])

    while q :
        t = q.pop(0)
        for k in range(4):
            nx = t[0] +dx[k]
            ny = t[1] +dy[k]
            if nx >= 0 and ny >=0 and nx < N and ny < N:
                if check[ny][nx] == 1 and time[ny][nx] > time[t[1]][t[0]]+ground[ny][nx] :
                    time[ny][nx] = time[t[1]][t[0]]+ground[ny][nx]
                    q.append([nx,ny])

                elif check[ny][nx] == 0:
                    time[ny][nx] += time[t[1]][t[0]]+ground[ny][nx]
                    check[ny][nx] = 1
                    q.append([nx,ny])

for tc in range(1, 1+T):
    N = int(input())
    ground = [list(map(int, input())) for _ in range(N)]
    time = [[0 for _ in range(N)] for __ in range(N)]
    check = [[0 for _ in range(N)] for __ in range(N)]
    q = []

    short(0,0)

    # for i in range(N):
    #     for j in range(N):
    #         print(time[i][j], end = ' ')
    #     print()

    print('#{} {}' .format(tc, time[N-1][N-1]))