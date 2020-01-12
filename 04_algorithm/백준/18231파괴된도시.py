import sys

sys.stdin = open('18231.txt')

N,M = map(int, input().split())

connect = [[0 for _ in range(N+1)] for _ in range(N+1)]

result = []

for _ in range(M):
    a,b = map(int, input().split())
    connect[a][b] = 1
    connect[b][a] = 1

des_num = int(input())
des_city = list(map(int, input().split()))

cities = [0 for _ in range(N+1)]
for k in range(des_num):
    cities[des_city[k]] = 1

# def power(n,k):
#     global flag, result
#     if flag:
#         return
#     if n == N+1 or k ==des_num:
#         visited = [0 for _ in range(N+1)]
#         for i in range(1,N+1):
#             if T[i] == 1:
#                 visited[i] = 1
#                 for j in range(N+1):
#                     if connect[i][j] ==1:
#                         visited[j] = 1
#
#         if visited == cities:
#             flag = 1
#             result = T[:]
#
#     else:
#         T[n] = 1
#         power(n+1,k+1)
#         T[n] = 0
#         power(n+1, k)

def power():
    1


T = [0 for _ in range(N+1)]
flag = 0
# power(1,0)

cnt = 0
city = []
for a in range(len(result)):
    if result[a] == 1:
        cnt +=1
        city.append(a)

if cnt:
    print(cnt)
    for i in city:
        print(i, end=' ')
else:
    print(-1)