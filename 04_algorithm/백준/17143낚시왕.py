import sys

sys.stdin = open("17143.txt")

R,C,M = map(int, input().split())

sharks = [list(map(int, input().split())) for _ in range(M)]

pool = [[0 for _ in range(C+1)] for _ in range(R+1)]
king = 0

dx =[0,0,0,1,-1]
dy =[0,-1,1,0,0]
ans = 0

visited = [[[0,0,0] for _ in range(C+1)] for _ in range(R+1)]
while king < C:
    for y,x,s,d,z in sharks:
        pool[y][x] = z
    # 1. 낚시왕 이동
    king +=1

    # 2. 상어 잡기
    for i in range(1,R+1):
        if pool[i][king]:
            ans += pool[i][king]
            pool[i][king] = 0
            break

    # 3. 상어 이동
    newshark = set()
    for j in range(len(sharks)):
        y,x,s,d,z = sharks[j]
        if pool[y][x]:
            tx,ty = x,y

            if d in [1,2]:
                re = R*2-2
            else :
                re = C*2-2

            rest = s%re

            for _ in range(rest):
                nx, ny = tx+dx[d], ty+dy[d]
                if not (0<nx<C+1 and 0<ny<R+1):
                    if d in [1,3]:
                        d += 1
                    elif d in [2,4]:
                        d -= 1
                    nx, ny = tx + dx[d], ty + dy[d]

                tx, ty = nx, ny

            if visited[ty][tx][2] < z:
                visited[ty][tx] = [s,d,z]

            newshark.add((ty,tx))
        pool[y][x] = 0

    sharks = []
    for y,x in newshark:
        sharks.append([y,x]+visited[y][x])
        visited[y][x] = [0,0,0]

print(ans)