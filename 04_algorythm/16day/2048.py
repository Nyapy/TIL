import sys

sys.stdin = open('2048.txt')

T = int(input())

def up():
    for j in range(N):
        i = 0
        a = -1
        tem = []
        zero = 0
        while i < N:
            if board[i][j] != 0 and a != board[i][j] and a == -1:
                 a = board[i][j]
            elif board[i][j] != 0 and a != board[i][j] and a >=0:
                 tem.append(a)
                 a = board[i][j]
            elif board[i][j] == a:
                tem.append(a*2)
                zero +=1
                a = -1
            elif board[i][j] == 0 :
                zero +=1
            i += 1
        if a != -1:
            tem.append(a)
        for i in range(zero):
            tem.append(0)
        trans.append(tem)

    for i in range(N):
        for j in range(N):
            board[i][j] = trans[j][i]

def down():
    for j in range(N-1, -1, -1):
        i = N-1
        a = -1
        tem = []
        zero = 0
        while i >= 0:
            if board[i][j] != 0 and a != board[i][j] and a == -1:
                 a = board[i][j]
            elif board[i][j] != 0 and a != board[i][j] and a >=0:
                 tem.insert(0,a)
                 a = board[i][j]
            elif board[i][j] == a:
                tem.insert(0,a*2)
                zero +=1
                a = -1
            elif board[i][j] == 0 :
                zero +=1
            i -= 1
        if a != -1:
            tem.insert(0,a)
        for i in range(zero):
            tem.insert(0,0)
        trans.insert(0,tem)
    for i in range(N):
        for j in range(N):
            board[i][j] = trans[j][i]

def left():
    for j in range(N):
        i = 0
        a = -1
        tem = []
        zero = 0
        while i < N:
            if board[j][i] != 0 and a != board[j][i] and a == -1:
                 a = board[j][i]
            elif board[j][i] != 0 and a != board[j][i] and a >=0:
                 tem.append(a)
                 a = board[j][i]
            elif board[j][i] == a:
                tem.append(a*2)
                zero +=1
                a = -1
            elif board[j][i] == 0 :
                zero +=1
            i += 1
        if a != -1:
            tem.append(a)
        for i in range(zero):
            tem.append(0)
        trans.append(tem)

    for i in range(N):
        for j in range(N):
            board[j][i] = trans[j][i]

def right():
    for j in range(N):
        i = N-1
        a = -1
        tem = []
        zero = 0
        while i >= 0:
            if board[j][i] != 0 and a != board[j][i] and a == -1:
                 a = board[j][i]
            elif board[j][i] != 0 and a != board[j][i] and a >=0:
                 tem.insert(0,a)
                 a = board[j][i]
            elif board[j][i] == a:
                tem.insert(0,a*2)
                zero +=1
                a = -1
            elif board[j][i] == 0 :
                zero +=1
            i -= 1
        if a != -1:
            tem.insert(0,a)
        for i in range(zero):
            tem.insert(0,0)
        trans.append(tem)

    for i in range(N):
        for j in range(N):
            board[j][i] = trans[j][i]



for tc in range(1,1+T):
    N, UDLR = input().split()
    N = int(N)
    board = [list(map(int, input().split())) for _ in range(N)]
    trans = []

    if UDLR == 'up':
        up()
    if UDLR == 'down':
        down()
    if UDLR == 'left':
        left()
    if UDLR == 'right':
        right()

    print('#{}' .format(tc))
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = ' ')
        print()
