import sys

sys.stdin = open('2636.txt')


from collections import deque
C, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(C)]
visited = [[0 for _ in range(R)] for _ in range(C)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def air(x,y):

    q = deque()
    q.append([x,y])
    visited[y][x] = 1

    while q:
        t = q.popleft()
        tx = t[0]
        ty = t[1]

        for k in range(4):
            nx = tx +dx[k]
            ny = ty +dy[k]

            if 0<=nx < R and 0 <= ny <C  and visited[ny][nx] == 0:
                if (board[ny][nx] == 0 or board[ny][nx] == -1):
                    q.append([nx,ny])
                    visited[ny][nx] = 1
                    board[ny][nx] = -1
                elif board[ny][nx] == 1:
                    cheese.add((nx,ny))

cnt = 0
for i in range(C):
    for j in range(R):
        if board[i][j]:
            cnt += 1


count = [cnt]
cheese = set()
air(0,0)

cheese = deque(cheese)
while cnt :
    next_cheese = set()
    cnt -= len(cheese)
    count.append(cnt)
    while cheese:
        t = cheese.popleft()
        tx = t[0]
        ty = t[1]
        board[ty][tx] = -1
        visited[ty][tx] = 1

        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]

            if 0 <= nx < R and 0 <= ny < C and visited[ny][nx] == 0:
                if (board[ny][nx] == 0 ):
                    cheese.append([nx, ny])
                    board[ny][nx] = -1
                elif board[ny][nx] == 1:
                    if (nx, ny) not in cheese:
                        next_cheese.add((nx,ny))
    cheese = deque(next_cheese)


print(len(count)-1)
print(count[-2])


