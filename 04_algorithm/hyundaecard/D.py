from collections import deque

falling = [[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]

board = [[0 for _ in range(7)] for _ in range(6)]

print(board)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def fall(line,color):
    tem = 0
    for i in range(6):
        if board[i][line] :
            break
        else:
            tem = i
    board[tem][line] = color

def bfs(x,y,c):
    visited = [[0 for _ in range(7)] for _ in range(6)]
    check = [[x,y]]
    visited[y][x] = 1
    q = deque()
    q.append([x,y])

    while q:
        tx, ty = q.popleft()

        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]

            if 0<= nx <7 and 0 <= ny < 6:
                if visited[ny][nx] == 0 and board[ny][nx] == c:

                    visited[ny][nx] = visited[ty][tx] + 1
                    q.append([nx,ny])
                    check.append(nx,ny)
                    tem = visited[ny][nx]
    if tem >=3:
        for i in range(len(tem)):
            del_x, del_y = tem[i]
            board[del_y][del_x] = 0

def drop() :


for i in falling:
    l, c = i
    fall(l,c)
