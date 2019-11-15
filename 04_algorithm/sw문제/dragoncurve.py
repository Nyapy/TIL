import sys
sys.stdin = open('dragoncurve.txt')

N = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dragons =[list(map(int, input().split())) for _ in range(N)]

G = [[0 for _ in range(102)] for _ in range(102)]


def dragoncurve(x,y,d,g):
    G[y][x] += 1
    gen = [d]
    nx = x +dx[gen[0]]
    ny = y +dy[gen[0]]
    gen = [(d+1)%4]
    curg = 0
    G[ny][nx] += 1
    x = nx
    y = ny
    while g > curg:
        for i in range(len(gen)):
            nx = x + dx[gen[i]]
            ny = y + dy[gen[i]]
            G[ny][nx] +=1
            x = nx
            y = ny
        tem = []
        for j in range(len(gen)-1,-1,-1):
            t =(1+gen[j])%4
            tem.append(t)
        gen = tem+gen
        x = nx
        y = ny
        curg+=1

cnt = 0
for d in range(len(dragons)):
    dragoncurve(dragons[d][0],dragons[d][1],dragons[d][2],dragons[d][3])

for i in range(101):
    for j in range(101):
        if G[i][j] != 0 and  G[i+1][j] != 0 and G[i][j+1] != 0 and G[i+1][j+1] != 0:
            cnt += 1

print(cnt)