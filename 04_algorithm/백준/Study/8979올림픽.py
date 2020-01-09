import sys

sys.stdin = open("8979.txt")

N, K = map(int, input().split())

rank = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    if rank[i][0] == K:
        T = rank[i]
        break

g,s,b = T[1],T[2],T[3]

result = 1

for i in range(N):
    if rank[i][1] > g:
        result += 1

    elif rank[i][1] == g and rank[i][2] > s :
        result += 1

    elif rank[i][1] == g and rank[i][2] == s and rank[i][3] > b:
        result += 1

print(result)