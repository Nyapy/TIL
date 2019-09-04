import sys

sys.stdin = open('오셀로.txt')

T = int(input())
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]


def othello(x,y,c):
    k = 0
    q = []
    if c == 1:
        while k < 8:
            flag = 0
            nx = x + dx[k]
            ny = y + dy[k]
            q= [[y, x]]
            while nx >=0 and ny >= 0 and nx <N and ny <N and nx<N:
                if board[ny][nx] == 1 and flag == 0:
                    break
                elif board[ny][nx] == 2:
                    flag =1
                    q.append([ny,nx])
                elif board[ny][nx] ==1 and flag == 1:
                    while q:
                        t = q.pop()
                        board[t[0]][t[1]] = 1
                    break
                elif board[ny][nx] == 0:
                    break
                nx = nx + dx[k]
                ny = ny + dy[k]
            k+=1

    elif c == 2:
        while k < 8:
            flag = 0
            nx = x + dx[k]
            ny = y + dy[k]
            q =[[y, x]]
            while nx >=0 and ny >= 0 and nx <N and ny <N and nx<N:
                if board[ny][nx] == 2 and flag == 0:
                    break
                elif board[ny][nx] == 1:
                    flag =1
                    q.append([ny,nx])
                elif board[ny][nx] ==2 and flag == 1:
                    while q:
                        t = q.pop()
                        board[t[0]][t[1]] = 2
                    break
                elif board[ny][nx] == 0:
                    break

                nx = nx +dx[k]
                ny = ny +dy[k]
            k += 1

for tc in range(1,1+T):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for __ in range(N)]
    board[N//2-1][N//2-1]=2
    board[N//2][N//2] = 2
    board[N//2][N//2 -1] = 1
    board[N//2 -1][N//2] = 1

    number = [list(map(int, input().split())) for _ in range(M)]

    for i in number:
        othello(i[0]-1,i[1]-1,i[2])
        # for i in range(N):
        #     for j in range(N):
        #         print(board[i][j], end=' ')
        #     print()
        # print()

    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] ==1:
                black += 1
            if board[i][j] == 2:
                white += 1

    print('#{} {} {}' .format(tc, black, white))