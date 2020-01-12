import sys
sys.stdin = open('16197두동전.txt')

N, M = map(int, input().split())

board = [list(input())for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

coin = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coin.append([j,i])
            board[i][j] = '.'

coin1 = coin[0]
coin2 = coin[1]

result = 11
def button(coina,coinb, dir, cnt):
    if cnt == 11:
        return
    global result
    co1x = coina[0] + dx[dir]
    co1y = coina[1] + dy[dir]

    co2x = coinb[0] + dx[dir]
    co2y = coinb[1] + dy[dir]

    flag = 0

    if 0 <= co1x < M and 0 <= co1y < N:
        if board[co1y][co1x] == '#':
            if dir in [0,1]:
                co1x = coina[0]
            elif dir in [2,3]:
                co1y = coina[1]
    else:
        flag +=1

    if 0 <= co2x < M and 0 <= co2y < N:
        if board[co2y][co2x] == '#':
            if dir in [0, 1]:
                co2x = coinb[0]
            elif dir in [2, 3]:
                co2y = coinb[1]
    else:
        flag += 1

    if flag == 0:
        for k in range(4):
            button([co1x,co1y],[co2x,co2y],k, cnt+1)

    elif flag == 1:
        if cnt < result :
            result = cnt

    elif flag ==2:
        return

for k in range(4):
    button(coin1, coin2, k, 1)

if result == 11:
    print(-1)
else:
    print(result)

