import sys
from time import time

sys.stdin = open("16235.txt")

start = time()
DIR = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

N, M, K = map(int, input().split())
MAP = [[5]*N for _ in range(N)]
tree_MAP = [[[] for _ in range(N)] for __ in range(N)]
energy = []
for _ in range(N):
    energy.append(list(map(int, input().split())))
for _ in range(M):
    x, y, c = map(int, input().split())
    tree_MAP[x-1][y-1].append(c)
for turn in range(K):
    # spting, summer
    grow = []
    for y in range(N):
        for x in range(N):
            if tree_MAP[y][x]:
                tree_MAP[y][x].sort()
                for i in range(len(tree_MAP[y][x])):
                    flag = 0
                    if MAP[y][x] < tree_MAP[y][x][i]: # 죽음
                        for j in range(len(tree_MAP[y][x])-1, i-1, -1):
                            MAP[y][x] += tree_MAP[y][x][j] // 2
                        del tree_MAP[y][x][j:]
                        break
                    else:
                        MAP[y][x] -= tree_MAP[y][x][i]
                        tree_MAP[y][x][i] += 1
                        if tree_MAP[y][x][i] % 5 == 0:
                            grow.append([y, x, tree_MAP[y][x][i]])

    # autumn
    for seed in grow:
        y, x, c = seed
        for c in DIR:
            Y = y+c[0]
            X = x+c[1]
            if 0 <= Y < N and 0 <= X < N:
                tree_MAP[Y][X].append(1)
    # winter
    for y in range(N):
        for x in range(N):
            MAP[y][x] += energy[y][x]
res = 0
for y in range(N):
    for x in range(N):
       if tree_MAP:
           res += len(tree_MAP[y][x])
print(res)
print(time()-start)