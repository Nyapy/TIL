import sys

sys.stdin = open('18231.txt')

N,M = map(int, input().split())

link = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    link[a][b] = 1
    link[b][a] = 1

K = int(input())
destroyed = list(map(int, input().split()))

destroyed_city = [0 for _  in range(N+1)]
visited =[0 for _ in range(N+1)]
boom = []

for i in destroyed:
    destroyed_city[i] = 1
    flag = 1
    for j in range(1, N+1):
        if link[i][j] == 1:
            if j in destroyed:
                continue
            else:
                flag = 0
    if flag:
        boom.append(i)


for i in boom:
    visited[i]= 1
    for j in range(1,N+1):
        if link[i][j] ==1:
            visited[j] = 1

flag = 1
for i in range(1, 1+N):
    if visited[i] != destroyed_city[i]:
        flag = 0
        break

if flag:
    boom.sort()
    print(len(boom))

    for i in boom:
        print(i, end=" ")
    print()


else:
    print(-1)