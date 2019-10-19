import sys

sys.stdin = open('등산로조성.txt')

T = int(input())

for tc in range(1,1+T):
    N, K = map(int, input().split())

    gido = [list(map(int, input().split())) for _ in range(N)]

    # print(gido)

    startx=0
    starty=0

    for i in range(N):
        for j in range(N):
            if gido[i][j] > gido[starty][startx]:
                startx = j
                starty = i
    hist = gido[starty][startx]
    start = []
    namu = []

    for i in range(N):
        for j in range(N):
            if gido[i][j] == hist:
                start += [[i,j]]

            else:
                namu += [[i,j]]

    # for a in range(namu):


    print(start)
    print(namu)