import sys

sys.stdin = open('makebridge.txt')

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def makeisland(x, y, inum):
    q = []
    Island[y][x] = inum
    q.append([x, y])

    while q:
        t = q.pop(0)
        for k in range(4):
            nx = t[0] + dx[k]
            ny = t[1] + dy[k]
            if 0 <= nx < M and 0 <= ny < N:
                if g[ny][nx] == 1 and Island[ny][nx] == 0:
                    Island[ny][nx] = inum
                    q.append([nx, ny])


def makebridge(x, y, inum):
    for k in range(4):
        dist = 0
        nx = x + dx[k]
        ny = y + dy[k]
        while 0 <= nx < M and 0 <= ny < N:
            if Island[ny][nx] == inum:
                break
            elif Island[ny][nx] == 0:
                dist += 1
                nx += dx[k]
                ny += dy[k]
            elif Island[ny][nx] != 0:
                if dist != 1:
                    if bridgedist[inum][Island[ny][nx]] > dist:
                        bridgedist[inum][Island[ny][nx]] = dist

                break


def MST(i):
    global total
    visited[i] = 1
    W = [100 for _ in range(inum)]

    t = i
    for _ in range(inum-2):
        for k in range(inum):
            if W[k] > bridgedist[t][k]:
                W[k] = bridgedist[t][k]

        small = 100
        for a in range(inum):
            if W[a] < small and visited[a] == 0:
                small = W[a]
                temp = a
        if small == 100:
            return -1
        total += small
        visited[temp] = 1
        t = temp
        visited[t] = 1
    return total

N, M = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(N)]
Island = [[0 for _ in range(M)] for _ in range(N)]

# print(g)
# print(Island)
inum = 1
for i in range(N):
    for j in range(M):
        if g[i][j] == 1 and Island[i][j] == 0:
            makeisland(j, i, inum)
            inum += 1

bridgedist = [[100 for _ in range(inum)] for _ in range(inum)]

for i in range(N):
    for j in range(M):
        if Island[i][j] != 0:
            makebridge(j, i, Island[i][j])

visited = [0 for _ in range(inum)]
total = 0
print(MST(1))