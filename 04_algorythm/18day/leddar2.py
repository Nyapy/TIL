import sys

sys.stdin = open('leddar2.txt')

T = 10

dx = [ 1, -1, 0]
dy = [ 0, 0, 1]

def leddar(x,y) :
    check[y][x] = 1
    q.append([x,y])
    while q:
        t = q.pop(0)

        for k in range(3):
            nx = t[0]+ dx[k]
            ny = t[1]+ dy[k]
            if nx >= 0 and ny >= 0 and nx <100 and ny < 100:
                if check[ny][nx] == 0 and laby[ny][nx] == 1:
                    check[ny][nx] = check[t[1]][t[0]]+1
                    q.append([nx,ny])
                    break

for tc in range(1, T+1):
    TC = int(input())
    laby = [list(map(int, input().split())) for _ in range(100)]
    heck = [[0 for _ in range(100)] for __ in range(100)]

    q =[]
    dist = 0
    min_dist = 10000
    start = 0

    for i in range(100):
        check = [[0 for _ in range(100)] for __ in range(100)]
        if laby[0][i] == 1:
            leddar(i,0)

        for j in range(100):
            if check[99][j] != 0:
                dist = check[99][j]
                break

        if dist < min_dist :
            min_dist = dist
            start = i

    print('#{} {}' .format(TC, start))