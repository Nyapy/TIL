import sys
sys.stdin = open("16235.txt")


N,M,K = map(int, input().split())

ntr = [list(map(int, input().split())) for _ in range(N)]

tem_trees = [list(map(int, input().split())) for _ in range(M)]

ground = [[5 for _ in range(N)] for _ in range(N)]

trees = dict()

dx = [-1,0,1,1,1,0,-1,-1]
dy = [-1,-1,-1,0,1,1,1,0]


for i in range(N):
    for j in range(N):
        trees[(j,i)] = []

for i in tem_trees:
    x,y,z = i
    trees.get((y-1,x-1)).append(z)

for codi, age in trees.items():
    age.sort()

for _ in range(K):
    spread = []
    for codi, tree in trees.items():
        for age in range(len(tree)):
            if tree[age] <= ground[codi[1]][codi[0]]:
                ground[codi[1]][codi[0]] -= tree[age]
                tree[age] += 1
                if tree[age]%5 == 0:
                    spread.append([codi[0],codi[1]])

            else:
                for j in tree[age:]:
                    ground[codi[1]][codi[0]] += j//2

                del tree[age:]
                # trees[codi] = tem
                break
    for info in spread:
        x,y = info

        for k in range(8):
            nx,ny = x+dx[k], y+dy[k]

            if 0<=nx<N and 0<=ny<N:
                trees.get((nx,ny)).insert(0,1)

    for i in range(N):
        for j in range(N):
            ground[i][j] += ntr[i][j]

ans = 0

for ages in trees.values():
    ans += len(ages)

print(ans)