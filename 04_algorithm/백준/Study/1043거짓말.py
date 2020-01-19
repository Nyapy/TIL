import sys

sys.stdin = open("1043.txt")


N, M = map(int, input().split())

truth = list(map(int, input().split()))
link = [[0 for _ in range(N+1)] for _ in range(N+1)]

party = [list(map(int, input().split())) for _ in range(M)]

cnt = 0

for i in range(M):
    tem =[0 for _ in range(N+1)]
    for j in range(1, len(party[i])):
        tem[party[i][j]] = 1
    for k in range(1,N+1):
        if tem[k] == 1:
            for l in range(1,N+1):
                if tem[l] == 1:
                    link[k][l] = 1
                    link[l][k] = 1

visited = [0 for _ in range(N+1)]
q =[]
for i in range(1,truth[0]+1):
    visited[truth[i]] = 1
    q.append(truth[i])

while q:
    t = q.pop(0)
    for k in range(1,N+1):
        if link[t][k] == 1 and visited[k] == 0:
            visited[k]=1
            q.append(k)

for i in range(M):
    flag = 1
    for j in range(1,len(party[i])):
        if visited[party[i][j]] == 1:
            flag = 0
            break
    if flag:
        cnt +=1

print(cnt)