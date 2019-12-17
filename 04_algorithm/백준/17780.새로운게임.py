import sys

sys.stdin = open("새로운게임.txt")


dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
mal = [list(map(int, input().split())) for _ in range(K)]



onmal = list(range(K+1))

visited = [[[] for _ in range(N)] for _ in range(N) ]

for a in range(K):
    visited[mal[a][0]-1][mal[a][1]-1] = [a+1]


def arae(k):
    if onmal[k] == k:
        return True
    return False

def move():
    result = 0
    while result <= 1000:
        result += 1
        for a in range(1,5):
            if arae(a):
                x = mal[a-1][1]-1
                y = mal[a-1][0]-1
                nx = x + dx[mal[a-1][2]]
                ny = y + dy[mal[a-1][2]]

                if 0 <= nx < N and 0 <= ny < N:
                    # 하얀 칸일 때
                    if board[ny][nx] == 0:
                        mal[a-1][1] = nx
                        mal[a-1][0] = ny
                        visited[ny][nx] += visited[y][x]
                        onmal[a] = visited[ny][nx][0]
                        visited[y][x] = []
                        if len(visited[ny][nx]) == 4:
                            return result

                    #빨간 칸일 때
                    elif board[ny][nx] == 1:
                        mal[a - 1][1] = nx
                        mal[a - 1][0] = ny
                        visited[ny][nx] += visited[y][x]

                        t = visited[ny][nx][-1]
                        onmal[visited[ny][nx][0]] = t
                        visited[ny][nx][-1] = visited[ny][nx][0]
                        visited[ny][nx][0] = t
                        onmal[t] = t

                        visited[y][x] = []

                    elif board[ny][nx] == 2:
                         if mal[a-1][2] == 1 or mal[a-1][2] == 3:
                             mal[a - 1][2] += 1
                         elif mal[a-1][2] ==2 or mal[a-1][2] == 4:
                             mal[a - 1][2] -= 1

                         nx = x + dx[mal[a - 1][2]]
                         ny = y + dy[mal[a - 1][2]]
                         if 0 <= nx < N and 0 <= ny < N and board[ny][nx] != 2 :
                             mal[a - 1][1] = nx
                             mal[a - 1][0] = ny
                             # 하얀 칸일 때
                             if board[ny][nx] == 0:
                                 mal[a - 1][1] = nx
                                 mal[a - 1][0] = ny
                                 visited[ny][nx] += visited[y][x]
                                 onmal[a] = visited[ny][nx][0]
                                 visited[y][x] = []
                                 if len(visited[ny][nx]) == 4:
                                     return result

                             # 빨간 칸일 때
                             elif board[ny][nx] == 1:
                                 mal[a - 1][1] = nx
                                 mal[a - 1][0] = ny
                                 visited[ny][nx] += visited[y][x]

                                 t = visited[ny][nx][-1]
                                 onmal[visited[ny][nx][0]] = t
                                 visited[ny][nx][-1] = visited[ny][nx][0]
                                 visited[ny][nx][0] = t
                                 onmal[t] = t

                                 visited[y][x] = []
                else:
                    if mal[a - 1][2] == 1 or mal[a - 1][2] == 3:
                        mal[a - 1][2] += 1
                    elif mal[a - 1][2] == 2 or mal[a - 1][2] == 4:
                        mal[a - 1][2] -= 1

                    nx = x + dx[mal[a - 1][2]]
                    ny = y + dy[mal[a - 1][2]]
                    if 0 <= nx < N and 0 <= ny < N and board[ny][nx] != 2:
                        mal[a - 1][1] = nx
                        mal[a - 1][0] = ny
                        # 하얀 칸일 때
                        if board[ny][nx] == 0:
                            mal[a - 1][1] = nx
                            mal[a - 1][0] = ny
                            visited[ny][nx] += visited[y][x]
                            onmal[a] = visited[ny][nx][0]
                            visited[y][x] = []
                            if len(visited[ny][nx]) == 4:
                                return result

                        # 빨간 칸일 때
                        elif board[ny][nx] == 1:
                            mal[a - 1][1] = nx
                            mal[a - 1][0] = ny
                            visited[ny][nx] += visited[y][x]

                            t = visited[ny][nx][-1]
                            onmal[visited[ny][nx][0]] = t
                            visited[ny][nx][-1] = visited[ny][nx][0]
                            visited[ny][nx][0] = t
                            onmal[t] = t

                            visited[y][x] = []

                    if len(visited[ny][nx]) == 4:
                        return result

    return -1

print(move())