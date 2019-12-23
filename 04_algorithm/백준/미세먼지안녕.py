import sys

sys.stdin = open("미세먼지안녕.txt")

R,C,T = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(R)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

upx = [1,0,-1,0]
upy = [0,-1,0,1]

dox = [1,0,-1,0]
doy = [0,1,0,-1]

def where():
    for i in range(R):
        for j in range(C):
            if A[i][j] == -1:
                return i


def diffusion():
    dusts =  [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if A[i][j] > 0 :
                dust = A[i][j]//5
                cnt = 0
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0<= nx <C and 0<= ny < R and A[ny][nx] != -1:
                        dusts[ny][nx] += dust
                        cnt += 1
                A[i][j] -= dust*cnt

    for i in range(R):
        for j in range(C):
            if dusts[i][j] != 0:
                A[i][j] += dusts[i][j]

def cleaner():
    k = 0

    x = air_cleaner[0]+ upx[k]
    y = air_cleaner[1]+ upy[k]

    nx = air_cleaner[0]+ upx[k]
    ny = air_cleaner[1]+ upy[k]

    before = 0
    current = 0

    while A[ny][nx] != -1:
        nx = x + upx[k]
        ny = y + upy[k]
        if nx <0 or ny < 0 or nx >=C or ny >= R:
            k+=1
            nx = x + upx[k]
            ny = y + upy[k]
        current = A[y][x]

        A[y][x] = before

        before = current

        x = nx
        y = ny
    k = 0

    x = air_cleaner2[0]+ dox[k]
    y = air_cleaner2[1]+ doy[k]

    nx = air_cleaner2[0]+ dox[k]
    ny = air_cleaner2[1]+ doy[k]

    before = 0
    current = 0
    while A[ny][nx] != -1:
        nx = x + dox[k]
        ny = y + doy[k]
        if nx < 0 or ny < 0 or nx >= C or ny >= R:
            k += 1
            nx = x + dox[k]
            ny = y + doy[k]
        current = A[y][x]

        A[y][x] = before

        before = current

        x = nx
        y = ny

air_cleaner = [0,where()]
air_cleaner2 = [0, air_cleaner[1]+1]

turn = 0
while turn < T:
    diffusion()
    cleaner()
    turn +=1

result = 0

for i in range(R):
    for j in range(C):
        if A[i][j] > 0:
            result += A[i][j]

print(result)