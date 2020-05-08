import sys

sys.stdin = open("5656.txt")
from collections import deque
from copy import deepcopy

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def breakblock(x, y):
    global visited, copyblock
    q = deque()
    q.append([x, y])
    while q:
        fx, fy = q.popleft()
        n = copyblock[fy][fx]
        copyblock[fy][fx] = 0
        if n >1:
            for k in range(4):
                nx, ny = fx, fy
                for _ in range(1, n):
                    nx, ny = nx + dx[k], ny + dy[k]
                    if 0 <= nx < W and 0 <= ny < H:
                        q.append([nx, ny])


def drop():
    global copyblock, ans
    new = []

    for g in range(W):
        tem = []
        for s in range(H):
            if copyblock[s][g]:
                tem.append(copyblock[s][g])
        new.append(tem)

    for g in range(W):
        tem = [0 for _ in range(H - len(new[g]))] + new[g]
        for h in range(H):
            copyblock[h][g] = tem[h]


def jperm(k):
    global copyblock, ans
    if ans == 0:
        return
    if k == N:
        copyblock = deepcopy(blocks)
        if db == [3,3,3]:
            sdsaf = 12312312
        for a in db:
            n = -1
            for b in range(H):
                if copyblock[b][a]:
                    n = b
                    break
            if n != -1:
                breakblock(a, n)
                drop()
        cnt = 0
        for i in range(H):
            for j in range(W):
                if copyblock[i][j]:
                    cnt += 1

        if cnt < ans:
            ans = cnt

        return
    else:
        for i in range(W):
            db[k] = i
            jperm(k + 1)


for tc in range(1, 1 + T):
    N, W, H = map(int, input().split())

    blocks = [list(map(int, input().split())) for _ in range(H)]
    copyblock = 1
    visited = 1

    db = [0] * N
    ans = W * H
    jperm(0)
    print("#{} {}".format(tc, ans))