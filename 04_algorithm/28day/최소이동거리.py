import sys

sys.stdin = open('최소이동거리.txt')

T = int(input())

def mst(v):
    q =[]
    visited[v] = 0
    u = v
    q.append(u)

    while q :
        t = q.pop(0)
        for i in range(N+1):
            if arr[t][i] != 0 and visited[i] > arr[t][i]+visited[t]:
                visited[i] = arr[t][i]+visited[t]
                q.append(i)

for tc in range(1,1+T):
    N,E = map(int, input().split())
    sew = [list(map(int, input().split())) for i in range(E)]
    arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [111111111]*(N+1)

    for i in sew:
        arr[i[0]][i[1]] = i[2]
    mst(0)

    print('#{} {}' .format(tc, visited[N]))