import sys

sys.stdin = open("2234.txt")

from collections import deque

m,n = map(int, input().split())

wall = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]

room = [[]]

nsize = []

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x,y,num):
    global largest
    large = 1
    visited[i][j] = num
    size = 1
    deq = deque()
    deq.append([x,y])

    while deq:
        t = deq.popleft()
        tx = t[0]
        ty = t[1]
        k = []
        for w in range(4):
            if wall[ty][tx] & (1 << w):
                pass
            else:
                k.append(w)

        for kk in k:
            nx = tx + dx[kk]
            ny = ty + dy[kk]
            if 0<= nx < m and 0 <= ny <n and visited[ny][nx] ==0:
                visited[ny][nx] =num
                deq.append([nx,ny])
                size += 1
                if large < size:
                    large = size
    if largest < large:
        largest = large
    nsize.append(large)
largest = 1
num = 1

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            bfs(j,i, num)
            num +=1


connect = [[0 for _ in range(num)] for _ in range(num)]

for i in range(n):
    for j in range(m):
        for k in [2,3]:
            nx = j + dx[k]
            ny = i + dy[k]
            if 0 <= nx < m and 0 <= ny < n and  visited[ny][nx] != visited[i][j]:
                connect[visited[ny][nx]][visited[i][j]] = 1


largest2 = 0
for i in range(1,num):
    for j in range(1, num):
        if connect[i][j] == 1:
            s = nsize[i-1]+ nsize[j-1]
            if s > largest2:
                largest2 = s

print(num-1)
print(largest)
print(largest2)