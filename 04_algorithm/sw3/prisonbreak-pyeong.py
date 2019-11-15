dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]

tp = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 1],
]


def b(y, x):
    global ret
    ret = 1
    q = [[y, x, 1]]
    visit[y][x] = 1
    while len(q):
        t = q.pop(0)
        if t[2] == L:
            return
        for i in range(4):
            tx = t[1] + dx[i]
            ty = t[0] + dy[i]
            if 0 <= tx < M and 0 <= ty < N and tp[m[t[0]][t[1]] - 1][i] and tp[m[ty][tx] - 1][3 - i] and visit[ty][
                tx] == 0 and m[ty][tx] != 0:
                visit[ty][tx] = t[2]
                q.append([ty, tx, t[2] + 1])
                ret += 1


T = int(input())
for i in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    ret = 0
    b(R, C)
    print("#{} {}".format(i, ret))