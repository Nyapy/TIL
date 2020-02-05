import sys

sys.stdin = open("13460.txt")

N,M = map(int, input().split())

board = [input() for _ in range(N)]

print(board)

dx = [0,1,0,-1]
dy = [-1,0,1,0]
#상우하좌
direction = 0

result = 11
def where():
    r = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                red = [j,i,1]
                r += 1
            elif board[i][j] == 'B':
                blue = [j,i,0]
                r+= 1
            if r == 2:
                return [red,blue]


def first(rx,ry,bx,by,d):
    flag = 0
    #빨강이 먼저면 flag =1
    if d == 0:
        if ry < by:
            flag = 1
    elif d == 1:
        if rx > by:
            flag = 1
    elif d == 2:
        if ry > by :
            flag = 1
    elif d == 3:
        if rx< bx :
            flag = 1
    return flag

def start(red, blue, k):
    global result
    if k == 11:
        return

    for i in range(4):
        succ = -1
        q=[]
        redx,redy,rc = red[0],red[1],1
        bluex,bluey, bc = blue[0],blue[1],0

        f=first(red[0], red[1], blue[0], blue[1], i)
        if f :
            q.append(red)
            q.append(blue)
        else:
            q.append(blue)
            q.append(red)

        while q:
            t= q.pop(0)
            nx = t[0]+dx[i]
            ny = t[1] +dy[i]
            c = t[2]

            if board[nx][ny] == '.' or board[nx][ny] == 'R' or board[nx][ny] == 'B':
                q.append([nx,ny,c])
                redx, redy = red[0], red[1]
                bluex, bluey = blue[0], blue[1]

            elif board[nx][ny] == 'O':
                if c == 1:
                    succ = 1
                elif c == 0:
                    succ = 0

        if succ ==1:
            if result > k:
                result = k
                return
        elif succ == 0:
            return
        start([redx,redy,rc],[bluex,bluey,bc],k+1)


a= where()

start(a[0], a[1], 1)

if result == 11:
    print(-1)
else:
    print(result)
