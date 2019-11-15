import sys

sys.stdin = open('최소신장트리.txt')

T = int(input())

def makeset(x):
    p[x] = x
    rank[x] = 0

def findset(x):
    if x == p[x]:
        return x
    else:
        return findset(p[x])

def union(x,y):
    link(findset(x), findset(y))

def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def kruskal(w):
    for j in nnw:
        if findset(j[0]) != findset(j[1]):
            w += j[2]
            union(j[0],j[1])

    return w

for tc in range(1,1+T):
    V, E = map(int,input().split())

    nnw = [list(map(int, input().split())) for _ in range(E)]
    nnw.sort(key=lambda x: x[2])

    p = [0]*(V+1)
    rank = [0] *(V+1)

    for i in range(V + 1):
        makeset(i)

    print('#{} {}' .format(tc, kruskal(0)))