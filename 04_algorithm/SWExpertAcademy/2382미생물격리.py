import sys
sys.stdin = open("2382.txt")

from collections import deque

T = int(input())

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for tc in range(1,1+T):
    N,M,K = map(int, input().split())

    micro = [list(map(int, input().split())) for _ in range(K)]
    q = deque()

    board = [[0 for _ in range(N)] for _ in range(N)]

    for a in micro:
        y,x,n,dir = a
        if dir == 1:
            dir = 1
        elif dir == 2:
            dir = 3
        elif dir == 3:
            dir = 0
        elif dir == 4:
            dir = 2

        board[y][x] = [[x,y,n,dir]]

    for time in range(M):

        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    n = 0
                    max_n = 0
                    dir = 0
                    for inf in board[i][j]:
                        n += inf[2]
                        if max_n < inf[2] :
                            max_n = inf[2]
                            dir = inf[3]

                    q.append([j,i,n,dir])
                    board[i][j] = 0


        while q:
            t = q.popleft()
            x,y,n,dir = t

            nx, ny = x+dx[dir], y+dy[dir]

            if nx in [0,N-1] or ny in [0,N-1]:
                n = n//2
                dir = (dir+2)%4

            if board[ny][nx] == 0:
                board[ny][nx] = [[nx,ny,n,dir]]

            else:
                board[ny][nx].append([nx,ny,n,dir])


    ans = 0
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                for inf in board[i][j]:
                    ans += inf[2]
    print("#{} {}" .format(tc, ans))
