import sys

sys.stdin = open("5650.txt")

from collections import deque
T = int(input())

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def pinball(x,y):
    q = deque()
    s= 0
    for k in range(4):
        if visited[y][x][k] < 0:
            q.append([x,y,k,s])
            visited[x][y][k] = 0

    while q:
        t = q.popleft()
        tx = t[0]
        ty = t[1]
        tk = t[2]
        sc = t[3]

        if sc < visited[ty][tx][tk]:
            continue

        nx = tx + dx[tk]
        ny = ty + dy[tk]


        if 0<= nx < N and 0 <= ny < N :
            if board[ny][nx] == 0:
                nk = tk

            elif board[ny][nx] == 1:
                if tk in [1,2]:
                    nk = (tk + 2) % 4
                    nx, ny = tx, ty
                elif tk == 0:
                    nk = 1
                elif tk == 3:
                    nk = 2
                sc +=1

            elif board[ny][nx] == 2:
                if tk in [2,3]:
                    nk = (tk + 2) % 4
                    nx, ny = tx, ty
                elif tk == 0:
                    nk = 3
                elif tk == 1:
                    nk = 2
                sc += 1

            elif board[ny][nx] == 3:
                if tk in [0,3]:
                    nk = (tk + 2) % 4
                    nx, ny = tx, ty
                elif tk == 1:
                    nk = 0
                elif tk == 2:
                    nk = 3
                sc += 1

            elif board[ny][nx] == 4:
                if tk in [0,1]:
                    nk = (tk + 2) % 4
                    nx, ny = tx, ty
                elif tk == 2:
                    nk = 1
                elif tk == 3:
                    nk = 0
                sc += 1

            elif board[ny][nx] == 5:
                nk = (tk+2)%4
                nx, ny = tx, ty
                sc += 1

            elif 5< board[ny][nx] < 11:
                for xx, yy in wormhall[board[i][j]]:
                    if nx != xx and ny != yy:
                        nx = xx
                        ny = yy
                        break
                nk = tk

            elif board[ny][nx] == -1:
                nk = tk


            if visited[ny][nx][nk] < sc :
                if board[ny][nx] != -1 and not (nx == x and ny == y) :
                    if board[ny][nx] == 0:
                        nk = tk

                    elif board[ny][nx] == 1:
                        if nk in [1, 2]:
                            nk = (tk + 2) % 4
                            nx, ny = tx, ty
                        elif nk == 0:
                            nk = 1
                        elif nk == 3:
                            nk = 2
                        sc += 1

                    elif board[ny][nx] == 2:
                        if nk in [2, 3]:
                            nk = (tk + 2) % 4
                            nx, ny = tx, ty
                        elif nk == 0:
                            nk = 3
                        elif nk == 1:
                            nk = 2
                        sc += 1

                    elif board[ny][nx] == 3:
                        if nk in [0, 3]:
                            nk = (tk + 2) % 4
                            nx, ny = tx, ty
                        elif nk == 1:
                            nk = 0
                        elif tk == 2:
                            nk = 3
                        sc += 1

                    elif board[ny][nx] == 4:
                        if nk in [0, 1]:
                            nk = (tk + 2) % 4
                            nx, ny = tx, ty
                        elif nk == 2:
                            nk = 1
                        elif nk == 3:
                            nk = 0
                        sc += 1

                    elif board[ny][nx] == 5:
                        nk = (tk + 2) % 4
                        nx, ny = tx, ty
                        sc += 1
                    q.append([nx,ny,nk,sc])
                    visited[ny][nx][nk] = sc
                else:
                    visited[ny][nx][nk] = sc

        else:
            nx = tx
            ny = ty
            nk = (tk+2)%4
            sc += 1

            if board[ny][nx] == 0:
                nk = tk

            elif board[ny][nx] == 1:
                if nk in [1,2]:
                    nk = (tk + 2) % 4
                    nx, ny = tx, ty
                elif nk == 0:
                    nk = 1
                elif nk == 3:
                    nk = 2
                sc +=1

            elif board[ny][nx] == 2:
                if nk in [2,3]:
                    nk = (tk + 2) % 4
                    nx, ny = tx, ty
                elif nk == 0:
                    nk = 3
                elif nk == 1:
                    nk = 2
                sc += 1

            elif board[ny][nx] == 3:
                if nk in [0,3]:
                    nk = (tk + 2) % 4
                    nx, ny = tx, ty
                elif nk == 1:
                    nk = 0
                elif tk == 2:
                    nk = 3
                sc += 1

            elif board[ny][nx] == 4:
                if nk in [0,1]:
                    nk = (tk + 2) % 4
                    nx, ny = tx, ty
                elif nk == 2:
                    nk = 1
                elif nk == 3:
                    nk = 0
                sc += 1

            elif board[ny][nx] == 5:
                nk = (tk+2)%4
                nx, ny = tx, ty
                sc += 1

            if visited[ny][nx][nk] < sc :
                if board[ny][nx] != -1 and not (nx == x and ny == y) :
                    q.append([nx,ny,nk,sc])
                    visited[ny][nx][nk] = sc
                else:
                    visited[ny][nx][nk] = sc


for tc in range(1,T+1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[[-1,-1,-1,-1] for _ in range(N)] for _ in range(N)]
    wormhall = [[] for _ in range(5)]
    for i in range(N):
        for j in range(N):
            if 5< board[i][j] < 11 :
                wormhall[board[i][j]-6].append([j,i])

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                pinball(j,i)

    for i in range(N):
        for j in range(N):
            for k in range(4):
                if board[i][j][k] > ans:
                    ans = board[i][j][k]


    print(board)