import sys
from time import time

sys.stdin = open("16235.txt")

start = time()

N,M,K = map(int, input().split())

ntr = [list(map(int, input().split())) for _ in range(N)]

tem_trees = [list(map(int, input().split())) for _ in range(M)]

ground = [[5 for _ in range(N)] for _ in range(N)]

trees = dict()

dx = [-1,0,1,1,1,0,-1,-1]
dy = [-1,-1,-1,0,1,1,1,0]


num_tree = len(tem_trees)

for i in range(num_tree):
    x,y,z = tem_trees[i]

    trees[(x-1,y-1)] = [z]

for codi, age in trees.items():
    age.sort()


def spring_summer():
    for codi, tree in trees.items():
        tem = []
        for age in range(len(tree)):
            if tree[age] <= ground[codi[1]][codi[0]]:
                ground[codi[1]][codi[0]] -= tree[age]
                tree[age] += 1
                tem.append(tree[age])
                if tree[age]%5 == 0:
                    spread.append([codi[0],codi[1],tree[age]])

            else:
                for j in tree[age:]:
                    ground[codi[1]][codi[0]] += j//2

                del tree[age:]
                # trees[codi] = tem
                break

def fall():
    tem = []

    for info in spread:
        x,y,age = info

        for k in range(8):
            nx,ny = x+dx[k], y+dy[k]

            if 0<=nx<N and 0<=ny<N:
                if trees.get((nx,ny)):
                    trees.get((nx,ny)).insert(0,1)
                else:
                    trees[(nx,ny)] = [1]

def winter():
    for i in range(N):
        for j in range(N):
            ground[i][j] += ntr[i][j]

for _ in range(K):
    spread = []
    spring_summer()
    fall()
    winter()

ans = 0

for ages in trees.values():
    ans += len(ages)

print(ans)
print(time()-start)