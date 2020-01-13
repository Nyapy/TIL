import sys

from collections import deque
sys.stdin = open("1389.txt")

N, M = map(int, input().split())

kevin = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    a,b = map(int, input().split())
    kevin[a][b] = 1
    kevin[b][a] = 1

tem = 9999999
result = 0
def bfs(v):
    global result,tem
    visited[v] = 1
    q = deque()
    q.append(v)
    bacon_number = 0
    while q:
        t =q.popleft()
        for i in range(1,N+1):
            if kevin[t][i] == 1 and visited[i] ==0 :
                visited[i] = visited[t]+1
                bacon_number += visited[t]
                q.append(i)
    if tem > bacon_number:
        tem = bacon_number
        result = v

for n in range(1,N+1):
    visited = [0 for _ in range(N+1)]
    bfs(n)

print(result)