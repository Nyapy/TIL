import sys
from collections import deque

sys.stdin = open("13460.txt")

N,M = map(int, input().split())

board = [list(input()) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

visited = [[[[0 for _ in range(10)] for _ in range(10)] for _ in range(10)]for _ in range(10)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            board[i][j] = '.'
            red = [j,i]
        elif board[i][j] == 'B':
            board[i][j] = '.'
            blue = [j, i]

q = deque()
visited[red[0]][red[1]][blue[0]][blue[1]] = 1
# print(board)
for k in range(4):
    q.append(red+blue+[k,0])

ans = -1

def first(rx,ry,bx,by,d):
    if d == 0:
        if rx < bx:
            return False
        else :
            return True
    elif d == 1:
        if ry < by :
            return False
        else:
            return True
    elif d == 2:
        if rx > bx:
            return False
        else:
            return True
    elif d == 3:
        if ry > by:
            return False
        else:
            return True
# print(q)
while q:
    rx, ry, bx, by, di, turn = q.popleft()
    if turn == 11:
        break
    flag = 1
    suc = 0

    f = first(rx,ry,bx,by,di)
    if f == False:
        tx, ty = rx,ry
        ax, ay = bx, by
        tx2, ty2 = bx, by

    else:
        tx, ty = bx,by
        ax, ay = rx, ry
        tx2, ty2 = rx, ry

    while flag:
        nx, ny = tx+dx[di], ty+dy[di]
        if board[ny][nx] == '#' or (nx == ax and ny == ay):
            if f == False:
                rx, ry = tx, ty
                ax, ay = tx, ty
            else:
                bx, by = tx, ty
                ax, ay = tx, ty

            break
        elif board[ny][nx] == '.':
            tx, ty = nx, ny

        elif board[ny][nx] == 'O':
            if f == False:
                suc = 1
            else:
                suc = 2
            break

    flag = 1

    while flag:
        nx2, ny2 = tx2+dx[di], ty2+dy[di]
        if board[ny2][nx2] == '#' or (nx2 == ax and ny2 == ay):
            if f == False:
                bx, by = tx2, ty2
            else:
                rx, ry = tx2, ty2
            break
        elif board[ny2][nx2] == '.':
            tx2, ty2 = nx2, ny2

        elif board[ny2][nx2] == 'O':
            if f == False:
                suc = 2
            else:
                suc = 1
            break

    if suc == 0:
        if visited[rx][ry][bx][by] == 0 :
            visited[rx][ry][bx][by] = turn+1
            for k in range(4):
                q.append([rx,ry,bx,by,k,turn+1])
    elif suc == 1:
        ans = turn+1
        break

print(ans)
