import sys

sys.stdin = open("17143.txt")

R,C,M = map(int, input().split())

dx = [0,0,1,-1]
dy = [-1,1,0,0]

sharks = [list(map(int, input().split())) for _ in range(M)]
pool = [[0 for _ in range(C+1)] for _ in range(R+1)]



king = 0
ans = 0

while king <C:
    for r, c, s, d, z in sharks:
        pool[r][c] = [r, c, s, d, z]

    king += 1
    for i in range(R+1):
        if pool[i][king]:
            ans += pool[i][king][4]
            pool[i][king] = 0
            break

    new = dict()
    visited = [[0 for _ in range(C + 1)] for _ in range(R + 1)]

    for r,c,s,d,z in sharks:
        if pool[r][c] == 0:
            continue
        pool[r][c] = 0
        x,y = c,r
        d -= 1
        tx, ty = c, r
        for sec in range(s):
            nx = tx + dx[d]
            ny = ty + dy[d]
            if not (0 <= nx < C+1 and 0 <= ny <R+1):
                d = (d+2)%4
                nx = tx + dx[d]
                ny = ty + dy[d]

            tx, ty = nx, ny
        if visited[ty][tx]:
            if visited[ny][tx] < z:
                new[(tx,ty)] = [ty,tx,s,d+1,z]
        else:
            visited[ty][tx] = z
            new[(tx, ty)] = [ty, tx, s, d+1,z]

    sharks = []
    for i in new.values():
        sharks.append(i)

print(ans)