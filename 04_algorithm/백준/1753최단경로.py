import sys
sys.stdin = open("1753.txt")

V,E = map(int, input().split())

K = int(input())

node = [dict() for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    if node[u].get(v):
        if node[u].get(v) > w:
            node[u][v] = w
    else:
        node[u][v] = w
# print(node)
W = [9999999]*(V+1)
visited = [0] *(V+1)
W[K] = 0

for _ in range(V):
    t = 99999999
    S = 0
    for i in range(1,V+1):
        if t > W[i] and visited[i] == 0:
            S = i
            t = W[i]
    if visited[S] == 0:
        visited[S] = 1
        for no,ga in node[S].items():
            if not visited[no] and W[no] > W[S]+ga:
                W[no] = W[S]+ga
#
for i in range(1,V+1):
    if W[i] == 9999999:
        print("INF")
    else:print(W[i])