import sys

sys.stdin = open('길찾기.txt')

T = 10

def search(v):
    Q = []
    visited[v] = 1
    Q.append(v)

    while Q :
        t = Q.pop(0)
        for i in range(len(gil)):
            if gil[t][i] == 1 and  visited[i] == 0 :
                visited[i] = 1
                Q.append(i)
                if i == 99:
                    return 1
    return 0

for tc in range(1, T+1):
    N, L = map(int, input().split())
    LL = list(map(int, input().split()))
    road = []
    gil = [[0 for _ in range(100)] for __ in range(100)]
    for i in range(0, len(LL), 2):
        gil[LL[i]][LL[i+1]] = 1
    visited = [0] *100

    print('#{} {}' .format(tc, search(0)))

