import sys
from time import time

sys.stdin = open("16235.txt")

start = time()

N, M, K = map(int, input().split())

ntr = [list(map(int, input().split())) for _ in range(N)]

tem_trees = [list(map(int, input().split())) for _ in range(M)]

ground = [[5 for _ in range(N)] for _ in range(N)]

trees = dict()
for y in range(N):
    for x in range(N):
        trees[(y, x)] = []

dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]

num_tree = len(tem_trees)

for i in range(num_tree):
    x, y, z = tem_trees[i]
    trees.get((x - 1, y - 1)).append(z)

for codi, age in trees.items():
    age.sort()

for _ in range(K):
    tem = []
    for codi, tree in trees.items():
        for age in range(len(tree)):
            if tree[age] <= ground[codi[0]][codi[1]]:
                ground[codi[0]][codi[1]] -= tree[age]
                tree[age] += 1
                if tree[age] % 5 == 0:
                    tem.append([codi[0], codi[1]])
            else:
                for j in tree[age:]:
                    ground[codi[0]][codi[1]] += j // 2
                del tree[age:]
                break
    for x, y in tem:  # fall
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                trees.get((nx, ny)).insert(0, 1)
    for i in range(N):
        for j in range(N):
            ground[i][j] += ntr[i][j]

ans = 0

for ages in trees.values():
    ans += len(ages)

print(ans)
print(time()-start)