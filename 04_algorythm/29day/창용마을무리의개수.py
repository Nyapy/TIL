import sys

sys.stdin = open('창용마을무리의개수.txt')

T = int(input())

def findset(x):
    if moory[x] == x:
        return x
    else:
        return findset(moory[x])

for tc in range(1,1+T):
    N,M = map(int, input().split())

    rel = [list(map(int, input().split())) for _ in range(M)]
    moory = list(range(N+1))

    for i in range(len(rel)):
        moory[findset(rel[i][1])] = findset(rel[i][0])
    cnt = 0
    for j in range(1,N+1):
        if moory[j] == j:
            cnt +=1

    print('#{} {}' .format(tc, cnt))