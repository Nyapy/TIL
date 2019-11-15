import sys

sys.stdin = open("prisonbreak.txt")


def cannext(t, k, next):
    if laby[t[1]][t[0]] == 1:
        if k == 0:
            if next in [1, 2, 5, 6]:
                return 1
        elif k == 1:
            if next in [1, 3, 6, 7]:
                return 1
        elif k == 2:
            if next in [1, 2, 4, 7]:
                return 1
        elif k == 3:
            if next in [1, 3, 4, 5]:
                return 1

    elif laby[t[1]][t[0]] == 2:
        if k == 0:
            if next in [1, 2, 5, 6]:
                return 1
        elif k == 2:
            if next in [1, 2, 4, 7]:
                return 1


    elif laby[t[1]][t[0]] == 3:
        if k == 1:
            if next in [1, 3, 6, 7]:
                return 1
        elif k == 3:
            if next in [1, 3, 4, 5]:
                return 1
    elif laby[t[1]][t[0]] == 4:
        if k == 0:
            if next in [1, 2, 5, 6]:
                return 1
        elif k == 1:
            if next in [1, 3, 6, 7]:
                return 1

    elif laby[t[1]][t[0]] == 5:
        if k == 1:
            if next in [1, 3, 6, 7]:
                return 1
        elif k == 2:
            if next in [1, 2, 4, 7]:
                return 1

    elif laby[t[1]][t[0]] == 6:
        if k == 2:
            if next in [1, 2, 4, 7]:
                return 1
        elif k == 3:
            if next in [1, 3, 4, 5]:
                return 1
    elif laby[t[1]][t[0]] == 7:
        if k == 0:
            if next in [1, 2, 5, 6]:
                return 1
        elif k == 3:
            if next in [1, 3, 4, 5]:
                return 1

    return 0


def prisonbreak(x,y, L):
    q.append([x,y])
    visited[y][x] = 1

    while q :
        t = q.pop(0)
        if 0 <= visited[t[1]][t[0]] < L:
            for k in range(4):
                nx = t[0] + dx[k]
                ny = t[1] + dy[k]

                if 0 <= nx < M and 0 <= ny <N:
                    if visited[ny][nx] == 0:
                        next = laby[ny][nx]
                        can = cannext(t, k, next)
                        if can :
                            q.append([nx,ny])
                            visited[ny][nx] = visited[t[1]][t[0]]+1



dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

T = int(input())

for tc in range(1,1+T):
    N, M, R, C, L = map(int, input().split())

    q = []
    laby = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0 for _ in range(M)] for __ in range(N)]

    cnt = 0

    prisonbreak(C,R, L)

    for i in range(N):
        for j in range(M):
            if visited[i][j] > 0:
                cnt += 1
    print("#{} {}" .format(tc, cnt))