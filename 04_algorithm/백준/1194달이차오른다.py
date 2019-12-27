import sys

sys.stdin = open("1194달이차오른다.txt")

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# N, M = map(int, input().split())
#
# laby = [list(input()) for _ in range(N)]
# visited = [[[N*M*64 for _ in range(M)] for _ in range(N)] for _ in range(64)]
#
# result = N*M*64
#
# for i in range(N):
#     for j in range(M):
#         if laby[i][j] == "0":
#             minsic = [j,i]
#             laby[i][j] = "."
#
# def bfs(x,y,d,dist):
#     global result
#     if result <= dist:
#         return
#     visited[d][y][x] =dist
#     q = []
#     q.append([x,y])
#
#     while q:
#         t = q.pop(0)
#         for k in range(4):
#             nx = t[0] + dx[k]
#             ny = t[1] + dy[k]
#
#             if 0<= nx <M and 0 <= ny <N and visited[d][ny][nx] == N*M*64:
#                 if laby[ny][nx] == '.':
#                     visited[d][ny][nx] = 1 + visited[d][t[1]][t[0]]
#                     q.append([nx,ny])
#
#                 elif 97 <= ord(laby[ny][nx]) <= 102:
#                     if (2**(ord(laby[ny][nx])-97) & d):
#                         visited[d][ny][nx] = 1 + visited[d][t[1]][t[0]]
#                         q.append([nx, ny])
#                     else:
#                         visited[d][ny][nx] = 1 + visited[d][t[1]][t[0]]
#                         tem = laby[ny][nx]
#                         laby[ny][nx] = '.'
#                         bfs(nx,ny,d+2**(ord(tem)-97), 1 + visited[d][t[1]][t[0]])
#                         laby[ny][nx] = tem
#                 elif 65 <= ord(laby[ny][nx]) <= 70:
#                     if (2**(ord(laby[ny][nx])-65))&d:
#                         visited[d][ny][nx] = 1 + visited[d][t[1]][t[0]]
#                         q.append([nx, ny])
#                 elif laby[ny][nx]== '1':
#                     visited[d][ny][nx] = visited[d][t[1]][t[0]]
#                     if visited[d][ny][nx] < result:
#                         result = visited[d][ny][nx]
#                     visited[d] = [[N * M * 64 for _ in range(M)] for _ in range(N)]
#                     return
#
# bfs(minsic[0],minsic[1],0,1)
#
# if result == N*M*64:
#     result = -1
#
# print(result)



dx = [-1,1,0,0]
dy = [0,0,-1,1]
N, M = map(int, input().split())
laby = [list(input()) for _ in range(N)]
visited = [[[999999 for _ in range(M)] for _ in range(N)] for _ in range(64)]
for i in range(N):
    for j in range(M):
        if laby[i][j] == "0":
            minsic = [j,i]
            laby[i][j] = "."



def bfs(x,y,d,dist):
    global result
    visited[d][y][x] = dist
    q = []
    q.append([x,y,0,0])
    while q:
        t = q.pop(0)
        for k in range(4):
            nx = t[0] + dx[k]
            ny = t[1] + dy[k]
            d = t[2]
            dist = t[3]
            if 0 <= nx <M and 0 <= ny <N :
                if laby[ny][nx] == '.':
                    if visited[d][ny][nx] > 1 + dist:
                        visited[d][ny][nx] = 1 + dist
                        q.append([nx, ny, d, 1+dist])
                elif 97 <= ord(laby[ny][nx]) <= 102:
                    if (2**(ord(laby[ny][nx])-97) & d):
                        if visited[d][ny][nx] > 1 + dist:
                            visited[d][ny][nx] = 1 + dist
                            q.append([nx, ny, d, 1+dist])
                    else:
                        tem = 2**(ord(laby[ny][nx])-97)
                        if visited[d+tem][ny][nx] > 1 + dist:
                            visited[d+tem][ny][nx] = 1 + dist
                            q.append([nx, ny, d+tem, 1+dist])
                elif 65 <= ord(laby[ny][nx]) <= 70:
                    if (2**(ord(laby[ny][nx])-65)) & d:
                        if visited[d][ny][nx] > 1 + dist:
                            visited[d][ny][nx] = 1 + dist
                            q.append([nx, ny, d, 1+dist])
                elif laby[ny][nx] == '1':
                    if visited[d][ny][nx] > 1+ dist:
                        visited[d][ny][nx] = 1+dist
                        if result > visited[d][ny][nx]:
                            result = visited[d][ny][nx]

result = 999999
bfs(minsic[0],minsic[1],0,0)
if result == 999999:
    result = -1
print(result)