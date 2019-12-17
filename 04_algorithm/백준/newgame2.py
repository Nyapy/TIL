import sys

sys.stdin = open('newgame2.txt')

dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]
N, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
board_on = [[[] for _ in range(N)] for _ in range(N) ]

mal = [0]+[list(map(int, input().split())) for _ in range(K)]
mal_on = list(range(K+1))

for i in range(1,K+1):
    mal[i][0] -= 1
    mal[i][1] -= 1

for z in range(1,1+K):
    board_on[mal[z][0]][mal[z][1]] += [z]

result = 987654321

def reverse(x, k, rev, bef):
    rev[k] = x
    if mal_on[x] == x:
        mal_on[x] = bef
        return
    else:
        reverse(mal_on[x], k+1, rev, x)
    mal_on[x] = bef

def white(x,y, nx, ny, num):
    rest = []
    bye = []
    flag = 0
    for a in board_on[y][x]:
        if a == num:
            if board_on[ny][nx]:
                mal_on[a] = board_on[ny][nx][-1]
            else:
                mal_on[a] = a
            flag = 1
        if flag == 1:
            bye += [a]
            mal[a][0] = ny
            mal[a][1] = nx
        else:
            rest += [a]
    board_on[ny][nx] += bye
    board_on[y][x] = rest

def red(x,y,nx,ny,num):
    rest = []
    bye = []
    flag = 0
    for a in board_on[y][x]:
        if a == num:
            mal_on[a] = a
            flag = 1
        if flag == 1:
            bye += [a]
            mal[a][0] = ny
            mal[a][1] = nx
        else:
            rest += [a]
    reverse(bye[-1], 0, bye, bye[-1])

    if board_on[ny][nx]:
        mal_on[bye[0]] = board_on[ny][nx][-1]
    else:
        mal_on[bye[0]] = bye[0]

    board_on[ny][nx] += bye
    board_on[y][x] = rest

def blue(x,y,nx,ny,num):
    if mal[num][2] == 1 or mal[num][2] ==3:
        mal[num][2] += 1
    else:
        mal[num][2] -= 1
    nx = x +dx[mal[num][2]]
    ny = y +dy[mal[num][2]]
    if 0 <= nx < N and 0 <= ny < N:
        if board[ny][nx] == 0:  # 하얀
            white(x, y, nx, ny, num)
        elif board[ny][nx] == 1:
            red(x, y, nx, ny, num)

def game():
    turn = 0
    while turn <= 1000:
        turn += 1
        for a in range(1,K+1):
            x = mal[a][1]
            y = mal[a][0]
            d = mal[a][2]

            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if board[ny][nx] == 0: #하얀
                    white(x,y,nx, ny, a)
                elif board[ny][nx] == 1:
                    red(x,y,nx,ny, a)
                else :
                    blue(x,y,nx,ny, a)

            else:
                blue(x,y,nx,ny, a)

            for i in range(N):
                for j in range(N):
                    if len(board_on[i][j]) >= 4:
                        return turn

    return -1

print(game())
