board = [[1,1,3,3],[4,1,3,4],[1,2,1,1],[2,1,3,2]]
from collections import deque
from copy import deepcopy


dx = [0,0,-1,1]
dy = [1,-1,0,0]
def hammer(x,y):
    copyboard[y][x]= 0
    tem = []
    for i in range(len(copyboard)):
        if copyboard[i][x] :
            tem.append(copyboard[i][x])
        copyboard[0][x] = 0
    for i in range(1,len(copyboard)-1):
        copyboard[i][x] = tem[i-1]

def candy(x,y):
    q = deque()

    visited[y][x] = 1
    q.append([x,y])

    val = copyboard[y][x]

    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]

            if 0<= nx < len(board[0]) and 0 <= ny <len(board):
                if visited[ny][nx] == 0 and copyboard[ny][nx] == val:
                    q.append([nx,ny])
                    visited[ny][nx]


for i in range(len(board)):
    for j in range(len(board[0])):
        copyboard = deepcopy(board)
        hammer()
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
