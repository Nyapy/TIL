import sys

sys.stdin = open("13460.txt")

N,M = map(int, input().split())

board = [list(input()) for _ in range(N)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]

red = [0,0,0]
blue = [0,0,1]

def where():
    g = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                red[0],red[1] = j,i
                board[i][j] = '.'
                g+=1
            elif board[i][j] == 'B':
                blue[0],blue[1] = j,i
                board[i][j] ='.'
                g+=1
            if g == 2:
                return

where()
print(red,blue)

def first(red,blue,direc):
    first = 0
    rx = red[0]
    ry = red[1]
    bx = blue[0]
    by = blue[1]

    if direc == 0:
        if by > ry:
            first = 1
    elif direc ==1:
        if bx < rx:
            first = 1
    elif direc == 2:
        if by < ry:
            first = 1
    elif direc == 3:
        if bx > rx:
            first = 1
    return first

def go(red,blue):
    global can
    turn = 1
    bids = [[red[0],red[1],0],[blue[0],blue[1],1],turn]
    q = []
    q.append(bids)

    while q:
        t= q.pop(0)
        red = t[0]
        blue = t[1]
        tu = t[2]

        for k in range(4):
            a = first(red,blue,k)
            if a:
                one = blue
                two = red
            else:
                one = red
                two = blue
            can = 0
            one = move(one[0],one[1],two[0],two[1],k,one[2])
            two = move(two[0],two[1],one[0],one[1],k,two[2])
            if can == 2:
                return tu
            elif can == 0:
                if tu+1 <= 10:
                    q.append([one,two,tu+1])
    return -1
def move(x,y, ex,ey, d, color):
    global can
    tx = x
    ty = y
    while 1:
        nx = tx + dx[d]
        ny = ty + dy[d]

        if board[ny][nx] == '#' or (nx == ex and ny == ey):
            return [tx,ty,color]

        elif board[ny][nx] == "O":
            if color == 0:
                can += 2
                return [tx,ty,color]
            else:
                can += 1
                return [tx,ty,color]

        else:
            tx = nx
            ty = ny

can = 0
print(go(red,blue))