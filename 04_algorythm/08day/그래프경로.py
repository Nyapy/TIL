import sys

sys.stdin = open('그래프경로_input.txt')

T = int(input())

def dfs(v):
    global cola

    visited[v] = 1
    # print(v, end=' ')
    if visited[G] == 1:
        cola = 1

    for w in range(V+1):
        if A[v][w] == 1 and visited[w] == 0:
            dfs(w)


for tc in range(1,T+1):

    cola = 0

    V, E = map(int, input().split())

    path = [list(map(int, input().split())) for _ in range(E)]

    S, G = map(int, input().split())
    # print(path)

    visited = [0 for _ in range(V+1)]

    A = [[0 for a in range(V+1)] for b in range(V+1)]

    for i in range(len(path)):
        A[path[i][0]][path[i][1]] = 1

    # for i in range(len(G)):
    #     for j in range(len(G[i])):
    #         print(G[i][j], end = ' ')
    #     print()
    dfs(S)
    print('#{} {}' .format(tc, cola))