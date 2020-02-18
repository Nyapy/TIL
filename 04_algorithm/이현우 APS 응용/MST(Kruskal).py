import sys

sys.stdin = open("MST.txt")


def unionset(x,y):
    vset[findset(x)] = vset[findset(y)]

def findset(v):
    if vset[v] == v:
        return v
    else:
        return findset(vset[v])

T = int(input())
for tc in range(1,T+1):
    V,G = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(G)]
    A.sort(key=lambda x:x[2])

    vset= list(range(V+1))

    result = 0
    cnt = 0
    for i in range(G):
        if findset(A[i][0]) != findset(A[i][1]):
            result += A[i][2]
            cnt += 1
        if cnt == V:
            break
    print(result)