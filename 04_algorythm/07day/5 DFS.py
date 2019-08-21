def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for w in range(V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

import sys
sys.stdin = open("그래프input.txt")

V, E = map(int,input().split()) #정점, 간선
temp = list(map(int,input().split()))

G = [[0 for _ in range(V+1)] for _ in range(V+1)]#이차원 초기화
visited = [0 for _ in range(V+1)]
print(visited)
print()

for i in range(0,len(temp),2):#입력
    G[temp[i]][temp[i+1]], G[temp[i+1]][temp[i]] = 1,1

for i in range(0,V+1):
    print('{} {}'.format(i, G[i]))

print()

dfs(1)