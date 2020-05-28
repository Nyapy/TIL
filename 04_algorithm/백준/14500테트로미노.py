import sys

sys.stdin = open("14500.txt")

from collections import deque


N,M = map(int, input().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

ans = 0

tetro = [[[(0,0),(1,0),(2,0),(3,0)]],[[(0,0),(0,1),(0,2),(0,3)]],
         [[(0,0),(1,0),(0,1),(1,1)]],
         [[(0,0),(0,1),(0,2),(1,2)], [(1,0),(1,1),(0,2),(1,2)], [(0,0),(1,0),(0,1),(0,2)], [(0,0),(1,0),(1,1),(1,2)]],
         [[(2,0),(0,1),(1,1),(2,1)], [(0,0),(0,1),(1,1),(2,1)], [(0,0),(1,0),(2,0),(2,1)], [(0,0),(1,0),(2,0),(0,1)]],
        [[(0,0),(0,1),(1,1),(1,2)], [(1,0),(1,1),(0,1),(0,2)]],
        [[(1,0),(2,0),(0,1),(1,1)], [(0,0),(1,0),(1,1),(2,1)]],
         [[(0,0),(0,1),(0,2),(1,1)], [(1,0),(1,1),(1,2),(0,1)]],
         [[(0,0),(1,0),(2,0),(1,1)], [(0,1),(1,1),(2,1),(1,0)]]
]

def cal(x,y,z):
    te = tetro[z]
    tem = 0
    for i in te:
        tem2 = 0
        for j in i:
            dx, dy = j
            nx, ny = x+dx, y+dy
            tem2 += paper[ny][nx]
        tem = max(tem,tem2)
    return tem
def mino(x,y):
    global ans
    tem = [ans]
    tem2 = 0
    if x+3 < M:
        tem.append(cal(x,y,0))
    if y+3 < N:
        tem.append(cal(x,y,1))
    if x+1 <M and y+1 <N:
        tem.append(cal(x,y,2))
    if x+1 <M and y+2 <N:
        for k in [3,5,7]:
            tem.append(cal(x,y,k))
    if x+2 <M and y+1 < N:
        for k in [4,6,8]:
            tem.append(cal(x,y,k))

    ans = max(tem)




for i in range(N):
    for j in range(M):
        mino(j,i)

print(ans)
# for i in tetro:
#     for j in i:
#         visited = [[0 for _ in range(M)] for _ in range(N)]
#         for k in j:
#             x,y = k
#             visited[y][x] = 1
#         for a in range(N):
#             print(visited[a])
#         print("naksdbkvlasbvidddddddddddddddddddddddddddddddddd")
