import sys

sys.stdin = open('최소합.txt')

T = int(input())
dx = [0,1]
dy = [1,0]

def bfs(i,j):
    dist[i][j] = board[i][j]
    q.append([i,j])

    while q:
        t = q.pop(0)
        for k in range(2):
            nx = t[1] + dx[k]
            ny = t[0] + dy[k]
            if nx >= 0 and ny >= 0 and nx < N and ny <N:

                if dist[ny][nx] > dist[t[0]][t[1]]+board[ny][nx]:
                    dist[ny][nx] = dist[t[0]][t[1]]+board[ny][nx]
                    q.append([ny, nx])

                elif dist[ny][nx] == 0:
                    dist[ny][nx] = dist[t[0]][t[1]] + board[ny][nx]
                    q.append([ny, nx])


for tc in range(1, 1+T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    q = []
    dist = [[0 for _ in range(N)] for __ in range(N)]

    bfs(0,0)
    print('#{} {}' .format(tc, dist[N-1][N-1]))