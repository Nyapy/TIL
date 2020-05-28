import sys
sys.stdin = open("1238.txt")

def party(s):
    W = [101 for _ in range(N+1)]
    W[s] =0
    visited = [0 for _ in range(N+1)]

    for i in range(M):
        g = 101
        t = 0
        for j in range(1,N+1):
            if j < g :
                g = W[j]
                t = j

        visited[t] = 1

        for k in range(1, N+1):
            if W[k] > road[t][k]:
                W[k] = road[t][k]


from collections import deque
N,M,X = map(int, input().split())

Times = [list(map(int, input().split())) for _ in range(M)]

road = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i,j,t in Times:
    road[i][j] = t

for st in range(1,N+1):
    party(st)


