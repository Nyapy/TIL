import sys

sys.stdin = open("MST.txt")

T = int(input())

def prim(v):
    result = 0
    ga[0] = 0
    for _ in range(G+1):
        tem = 9999999
        for i in range(G+1):
            if visited[i]==0 and tem > ga[i]:
                tem = ga[i]
                u = i

        visited[u] =1
        result += ga[u]

        for j in range(G+1):
            if arr[u][j]:
                if ga[j] > arr[u][j]:
                    ga[j] = arr[u][j]

    print("#{} {}" .format(tc,result))

for tc in range(1,T+1):
    G,V = map(int, input().split())
    arr = [[0 for _ in range(G+1)] for _ in range(G+1)]

    for a in range(V):
        A = list(map(int, input().split()))
        arr[A[0]][A[1]] = A[2]
        arr[A[1]][A[0]] = A[2]
    ga = [9999999 for _ in range(G+1)]

    visited = [0 for _ in range(G+1)]

    prim(0)