import sys

sys.stdin = open('최소신장트리.txt')

T = int(input())

def prim(v):
    total = 0
    u = v
    for a in range(V+1):
        minv = 1111111111111
        gajoong[u] = 0
        visited[u] = 1

        for i in range(V+1):
            if gajoong[i]!= 0 and visited[i] == 0 and line[u][i] != 0 and line[u][i] < gajoong[i]:
                gajoong[i] = line[u][i]

        for j in range(V+1):
            if gajoong[j] != 0 and gajoong[j] < minv:
                minv = gajoong[j]
                u = j

        if minv == 1111111111111:
            continue
        total += minv

    return total

for tc in range(1,1+T):
    V, E = map(int,input().split())

    nnw = [list(map(int, input().split())) for _ in range(E)]
    line = [[0 for i in range(V+1)] for _ in range(V+1)]
    visited = [0] *(V+1)
    gajoong = [100000000] *(V+1)

    for i in range(len(nnw)):
        line[nnw[i][0]][nnw[i][1]] = nnw[i][2]
        line[nnw[i][1]][nnw[i][0]] = nnw[i][2]

    print('#{} {}' .format(tc, prim(0)))