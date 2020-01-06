import sys

sys.stdin = open("2606바이러스.txt")

com_n = int(input())
pair_n = int(input())

pair = [list(map(int, input().split())) for _ in range(pair_n)]

visited = [0 for _ in range(com_n+1)]

network = [[0 for _ in range(com_n+1)] for _ in range(com_n+1)]

for i in range(pair_n):
    y = pair[i][0]
    x = pair[i][1]
    network[y][x] = 1
    network[x][y] = 1

def virus(com):
    visited[com] = 1

    for i in range(1, com_n+1):
        if visited[i] == 0 and network[com][i] == 1:
            virus(i)

virus(1)

cnt = 0
for k in range(1, com_n+1):
    if visited[k] == 1:
        cnt +=1

print(cnt-1)