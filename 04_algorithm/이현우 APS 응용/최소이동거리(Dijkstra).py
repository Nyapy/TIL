import sys
import time
sys.stdin = open("최소이동거리.txt")



# 단방향임에 주의할것!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


str_time = time.time()
T = int(input())

def dijkstra(v):
    ga[v] = 0

    while not visited[V]:
        tem = 99999999
        u = 0
        for i in range(V+1):
            if visited[i]==0 and ga[i] < tem:
                tem = ga[i]
                u = i
        visited[u] =1

        for j in range(V+1):
            if ga[j] > arr[u][j]+ga[u]:
                ga[j] = arr[u][j]+ga[u]

for tc in range(1,T+1):
    V,G = map(int,input().split())
    arr = [[999999 for _ in range(V+1)] for _ in range(V+1)]

    ga =[9999999 for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for i in range(G):
        A = list(map(int, input().split()))
        arr[A[0]][A[1]] = A[2]
        # arr[A[1]][A[0]] = A[2]

    dijkstra(0)

    print("#{} {}" .format(tc, ga[V]))

print(time.time()-str_time)