import sys
sys.stdin = open('dragoncurve.txt')

N = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x,y,d,g = map(int, input().split())

G = [[0 for _ in range(100)] for _ in range(100)]

print(x,y,d,g)

def dragoncurve(x,y,d,g):
    G[y][x] += 1
    gen = [d]
    nx= x + dx[gen[d]]
    ny= y + dy[gen[d]]
    G[ny][nx] += 1
    gen = [d+1]

    curg = 0
    while g >= curg:
        for i in range(len(gen)):
            tem = []
            nx = x + dx[gen[i]]
            ny = y + dy[gen[i]]
            G[ny][nx] +=1

        for j in range(len(gen)-1, -1, -1):
            tem.append((4+gen[j]-1)%4)
        gen += tem

        x = nx
        y = ny

cnt = 0
dragoncurve(x,y,d,g)

for i in range(100):
    for j in range(100):
        if G[i][j] != 0 and  G[i+1][j] != 0 and G[i][j+1] != 0 and G[i+1][j+1] != 0:
            cnt += 1

print(cnt)