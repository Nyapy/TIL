from collections import deque
import sys
from copy import deepcopy


def bfs():
    Q = deque([(0, 0, 0, K)])
    while Q:
        d, x, y, po = Q.popleft()
        for dx, dy in dr2:
            tx, ty = x + dx, y + dy
            if 0 <= tx < W and 0 <= ty < H and not ml[po][ty][tx]:
                ml[po][ty][tx] = 1
                if tx == gx and ty == gy:
                    return d+1
                else:
                    Q.append([d+1, tx, ty, po])
        if po:
            po -= 1
            for dx, dy in dr:
                tx, ty = x + dx, y + dy
                if 0 <= tx < W and 0 <= ty < H and not ml[po][ty][tx]:
                    ml[po][ty][tx] = 1
                    if tx == gx and ty == gy:
                        return d+1
                    else:
                        Q.append([d+1, tx, ty, po])
    return 0


K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
nl = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
ml = []
for k in range(K+1):
    ml.append(deepcopy(nl))
for k in range(K+1):
    ml[k][0][0] = 1
gx, gy = W-1, H-1

if gx or gy:
    dr = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
    dr2 = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    tmp = bfs()
    if tmp:
        print(tmp)
    else:
        print(-1)
else:
    print(0)

