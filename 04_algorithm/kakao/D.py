board = [[0,0,0,0,0,0,0,1,1,1],
        [0,1,1,1,1,1,0,1,1,1],
        [0,0,0,1,1,1,0,1,1,1],
        [1,1,0,1,1,0,0,1,1,1],
        [0,0,0,1,1,0,1,1,1,1],
        [0,1,1,1,1,0,0,1,1,1],
        [0,1,1,1,1,1,0,1,1,1],
        [0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,0],
        [1,1,1,1,1,1,1,1,1,0],
    ]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

N = len(board[0])
visited = [[9999999 for _ in range(N)] for _ in range(N)]

x, y = 0, 0
q = []
q.append([x,y])
visited[0][0] = 0
while q:
    fx, fy = q.pop(0)
    corner = 1
    for k in range(4):
        direct = 1
        tx, ty = fx, fy
        while direct:
            if not (fx == 0 and fy == 0) and corner:
                visited[fy][fx] += 500
                corner = 0
            nx, ny = tx +dx[k], ty +dy[k]
            if 0<= nx < N and 0 <= ny <N and visited[ny][nx] >= visited[ty][tx]+100 and board[ny][nx] == 0:
                visited[ny][nx] = visited[ty][tx]+100
                tx, ty = nx , ny
                if not (nx == N-1 and ny == N-1):
                    q.append([tx,ty])
            else:
                direct = 0

print(visited[N-1][N-1])


# import sys
# sys.setrecursionlimit(10000)
#
# res = 0
#
# DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# def dfs(y, x, scr, arr, board, length, visited, corner):
#     global res
#     if y == length-1 and x == length-1:
#         if res > scr+(corner*500):
#             res = scr+(corner*500)
#         return
#     if scr+(corner*500) >= res:
#         return
#     for i in range(len(DIR)):
#         Y = y+DIR[i][0]
#         X = x+DIR[i][1]
#         if 0 <= Y < length and 0 <= X < length and board[Y][X] == 0:
#             if i == arr or arr == -1:
#                 if visited[i][Y][X] > scr+100 + (corner*500):
#                     visited[i][Y][X] = scr+100 + (corner*500)
#                     dfs(Y, X, scr+100, i, board, length, visited, corner)
#             else:
#                 if visited[i][Y][X] > scr+600 + (corner*500):
#                     visited[i][Y][X] = scr+600 + (corner*500)
#                     dfs(Y, X, scr+100, i, board, length, visited, corner+1)
#
#
# def solution(board):
#     global res
#     answer = 0
#     length = len(board[0])
#     res = 2000*length*length
#     visited = [[[res] * length for _ in range(length)] for _ in range(4)]
#     visited[0][0][0] = 0
#     visited[1][0][0] = 0
#     visited[2][0][0] = 0
#     visited[3][0][0] = 0
#     dfs(0, 0, 0, -1, board, length, visited, 0)
#     answer = min(visited[0][length-1][length-1], visited[1][length-1][length-1], visited[2][length-1][length-1], visited[3][length-1][length-1])
#     return answer