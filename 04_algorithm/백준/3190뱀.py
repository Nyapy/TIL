import sys

sys.stdin = open("3190.txt")

N = int(input())

K = int(input())

apples = [list(map(int, input().split())) for _ in range(K)]

L = int(input())
XC = [list(input().split()) for _ in range(L)]
# print(XC)

snake_len = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]

board = [[0 for _ in range(N)] for _ in range(N)]

for i in range(len(XC)):
    XC[i][0] = int(XC[i][0])

# print(XC)
for a,b in apples:
    board[a-1][b-1] = 2

seq = []
snake_head = [0,0]
tail = 0
direction = 0

time = 0
next = 0
board[0][0] = 1
while 1:
    time += 1

    tx, ty = snake_head
    seq.append([tx,ty])

    nx,ny = tx+dx[direction], ty+dy[direction]

    if 0<=nx<N and 0<=ny<N:
        if board[ny][nx] == 0:
            board[ny][nx] = 1
            snake_head = [nx, ny]
            board[seq[tail][1]][seq[tail][0]] = 0
            tail += 1
        elif board[ny][nx] == 1:
            break
        elif board[ny][nx] == 2:
            board[ny][nx] = 1
            snake_head =[nx, ny]
        board[ny][nx] = 1

    else:
        break
    if next < len(XC) and time == XC[next][0] :
        if XC[next][1] == 'L':
            direction = (direction+3)%4
        else:
            direction = (direction+1)%4
        next += 1

print(time)