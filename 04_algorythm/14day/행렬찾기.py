import sys

sys.stdin = open('행렬찾기.txt')

T = int(input())
dx = [1, 0]
dy = [0, 1]

def search(x,y):
    q=[]
    check[x][y] = 1
    q.append([x,y])
    mx = 0
    my = 0

    while q:
        t = q.pop(0)

        for k in range(2):
            nx = t[0] + dx[k]
            ny = t[1] + dy[k]
            if nx >= 0 and ny >= 0 and nx <n and nx <n :
                if chem[nx][ny] !=0 and check[nx][ny] ==0:
                    check[nx][ny] = 1 +check[t[0]][t[1]]
                    q.append([nx,ny])
                    if mx < nx :
                        mx = nx
                    if my < ny :
                        my = ny
    row = mx - x +1
    col = my - y +1

    hang.append([row*col,row,col])

for tc in range(1, T+1):
    n = int(input())
    chem = [list(map(int, input().split())) for __ in range(n)]
    check = [[0 for _ in range(n)] for __ in range(n)]
    hang = []
    ans = []

    for i in range(n):
        for j in range(n):
            if chem[i][j] != 0 and check[i][j] == 0:
                search(i,j)

    hang.sort()
    ans += [len(hang)]

    for i in range(len(hang)):
        ans += [hang[i][1], hang[i][2]]

    print('#{}'.format(tc), end = ' ')
    for i in ans:
        print(i, end= ' ')
    print()



