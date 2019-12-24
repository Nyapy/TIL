import sys

sys.stdin = open("아기상어.txt")

N = int(input())

space = [list(map(int, input().split())) for _ in range(N)]

dx = [0,-1, 1,0]
dy = [-1,0,0,1]

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            shark = [j,i,2,0]
            space[i][j] = 0



def bfs(x,y):
    sea[y][x] = 1
    q = []
    q.append([x,y])
    while q :
        t = q.pop(0)

        for k in range(4):
            nx = t[0] + dx[k]
            ny = t[1] + dy[k]

            if 0<= nx <N and 0 <= ny <N and sea[ny][nx] == 0 and space[ny][nx] <= shark[2]:
                q.append([nx,ny])
                sea[ny][nx] = sea[t[1]][t[0]]+1
                if 0 < space[ny][nx] < shark[2]:
                    dist[sea[t[1]][t[0]]] += [[nx,ny]]

def eat():
    x= N
    y = N
    flag = 0
    for a in range(N**2):
        for b in range(len(dist[a])):
            if dist[a][b]:
                flag = 1
                if y > dist[a][b][1]:
                    x = dist[a][b][0]
                    y = dist[a][b][1]
                elif y == dist[a][b][1]:
                    if x >dist[a][b][0]:
                        x = dist[a][b][0]
                        y = dist[a][b][1]
        if flag == 1:
            space[y][x] = 0
            return (x,y,a)
    return 0

time = 0

mother_call = 1
while mother_call:
    sea = [[0 for _ in range(N)] for _ in range(N)]
    dist = [[] for _ in range(N**2)]

    bfs(shark[0],shark[1])
    A = eat()
    if A :
        shark[0] = A[0]
        shark[1] = A[1]
        shark[3] += 1
        time += A[2]

        if shark[3] == shark[2]:
            shark[2] += 1
            shark[3] = 0
    else:
        mother_call = 0

print(time)