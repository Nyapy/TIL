import sys

sys.stdin = open('상원이의 생일파티.txt')

T = int(input())

def invite(v):
    visited[v] = 1
    q.append(v)

    while q:
        t = q.pop(0)
        for w in range(N+1):
            if link[t][w] == 1 and visited[w]==0:
                visited[w] = visited[t]+1
                q.append(w)

for tc in range(1, T+1):
    N,M = map(int, input().split())

    fri = [list(map(int, input().split())) for _ in range(M)]
    link = [[0 for _ in range(N+1)] for __ in range(N+1)]

    for i in fri:
        link[i[0]][i[1]] = 1
        link[i[1]][i[0]] = 1

    visited = [0] * (N+1)
    cnt = 0
    q = []
    invite(1)

    for i in range(2, N+1):
        if visited[i] <= 3 and visited[i] >0:
            cnt += 1


    print('#{} {}' .format(tc, cnt))