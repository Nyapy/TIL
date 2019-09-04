import sys

sys.stdin = open('어디에 단어가 들어갈 수 있을까.txt')

T = int(input())

dx = [1, 0]
dy = [0, 1]

def crossword1(y,x):
    global cnt
    k = 0
    while k < 1:
        leng = 1
        nx = x + dx[k]
        ny = y + dy[k]
        while nx >= 0 and ny >= 0 and nx < N and ny <N :
            check[ny][nx] = 1
            if puzzle[ny][nx] == 0 and leng > K:
                break
            elif puzzle[ny][nx] == 0 and leng < K :
                break
            elif puzzle[ny][nx] == 1:
                leng +=1
            elif puzzle[ny][nx] == 0 and leng == K:
                cnt += 1
                break

            nx = nx +dx[k]
            ny = ny +dy[k]

            if nx == N and leng == K:
                cnt += 1
            if ny == N and leng == K:
                cnt += 1

        k+=1

def crossword2(y,x):
    global cnt
    k = 1
    while k < 2:
        leng = 1
        nx = x + dx[k]
        ny = y + dy[k]
        while nx >= 0 and ny >= 0 and nx < N and ny <N :
            check[ny][nx] = 1
            if puzzle[ny][nx] == 0 and leng > K:
                break
            elif puzzle[ny][nx] == 0 and leng < K :
                break
            elif puzzle[ny][nx] == 1:
                leng +=1
            elif puzzle[ny][nx] == 0 and leng == K:
                cnt += 1
                break

            nx = nx +dx[k]
            ny = ny +dy[k]

            if nx == N and leng == K:
                cnt += 1
            if ny == N and leng == K:
                cnt += 1

        k+=1

for tc in range(1,T+1):
    N,K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    check = [[0 for _ in range(N)] for __ in range(N)]

    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1 and check[i][j] == 0  :
                crossword1(i,j)


    check = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1 and check[i][j] == 0  :
                crossword2(i,j)

    print('#{} {}' .format(tc, cnt))