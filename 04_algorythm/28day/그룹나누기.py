T = int(input())

def findset(x):
    if x == p[x]:
        return x
    else:
        return findset(p[x])
def union(x,y):
    p[findset(y)]  = findset(x)

for tc in range(1, T+1):
    N,M = map(int, input().split())
    cnt = 0

    number = list(map(int, input().split()))

    sinch = []

    p = list(range(N+1))

    for i in range(0, len(number), 2):
        sinch +=[[number[i], number[i+1]]]

    for j in sinch:
        union(j[0], j[1])
    ans = set()
    for i in range(1, N+1):
        ans.add(findset(i))

    print('#{} {}' .format(tc, len(ans)))