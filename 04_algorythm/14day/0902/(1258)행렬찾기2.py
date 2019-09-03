def get_submatrix(x, y):
    global submatrix
    r, c  = 0, 0
    while data[x + r][y]: r += 1  #행
    while data[x][y + c]: c += 1  #열

    #clear
    for i in range(r):
        for j in range(c):
          data[x+i][y+j] = 0

    submatrix.append([r, c])

import sys
sys.stdin = open("(1258)행렬찾기_input.txt","r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    submatrix = []

    for i in range(N):
        for j in range(N):
            if data[i][j]:
                get_submatrix(i, j)

    submatrix.sort(key=lambda a:(a[0]*a[1], a[0]))

    print(f"#{tc+1} {len(submatrix)}", end=" ")
    for i in range(len(submatrix)):
        print(f"{submatrix[i][0]} {submatrix[i][1]}", end=" ")
    print()
