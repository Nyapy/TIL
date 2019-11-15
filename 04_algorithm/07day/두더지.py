def mole(q, w, cnt):
    if ternel[q][w] == 1 and check[q][w] == 0:
        count.append(cnt)
        check[q][w] = cnt

        for a in range(4):
            x = q + dy[a]
            y = w + dx[a]
            if x >= 0 and y >= 0 and x < n and y <n:
                mole(x, y, cnt)

import sys
sys.stdin = open('두더지.txt')

n = int(input())

ternel = [list(map(int, input().split())) for _ in range(n)]

check = [[0 for _ in range(n)] for _ in range(n)]

num = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

count = []
cnt = 0

for i in range(len(ternel)):
    for j in range(len(ternel[i])) :
        if ternel[i][j] == 1 and check[i][j] == 0:
            cnt += 1
        mole(i, j, cnt)

A = set(count)
B =[]

for j in A:

    cnt = 0
    for i in count:
        if i == j:
            cnt +=1
    B.append(cnt)
print(len(A))
print(sorted(B))