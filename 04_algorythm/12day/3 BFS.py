import sys

sys.stdin = open('BFS.txt')

def BFS(v):
    visited[v] = 1
    queue.append(v)
    print(v)

    while queue:
        t = queue.pop(0)

        for i in range(len(G[t])):
            if visited[i] == 0 and G[t][i] ==1:
                queue.append(i)
                visited[i] = visited[t]+1
                print(i)

n, l = map(int, input().split())
tem = [list(map(int, input().split())) for _ in range(l)]


G = [[0 for _ in range(n+1)] for __ in range(n+1)]
visited = [0]*(n+1)
queue = []

for i in range(len(tem)):
    G[tem[i][0]][tem[i][1]] = 1
    G[tem[i][1]][tem[i][0]] = 1



BFS(1)

# print(max(visited))

print(visited)
for i in range(len(visited)):
    if visited[i] == max(visited):
        print(i)