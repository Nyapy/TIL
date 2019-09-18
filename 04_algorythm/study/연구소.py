import sys, copy

sys.stdin = open('연구소.txt')

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def virus(y,x):
    check[y][x] = 1
    for k in range(4):
        nx = x +dx[k]
        ny = y +dy[k]
        if nx >= 0 and ny >= 0 and nx <M and ny <N:
            if lab1[ny][nx] == 0:
                if check[ny][nx] == 0:
                    lab1[ny][nx] = 2
                    virus(ny,nx)

def threewall(q):
    global max_safe
    for i in range(3):
        lab1[T[i][0]][T[i][1]] = 1

    for y in range(N):
        for x in range(M):
            if lab1[y][x] == 2:
                if check[y][x] == 0:
                    virus(y,x)
    safe = 0
    for y in range(N):
        for x in range(M):
            if lab1[y][x] == 0:
                safe += 1
    if safe > max_safe:
        max_safe = safe

def comb(n,r,q):
    global lab1, check
    if r == 0:
        lab1 = copy.deepcopy(lab)
        check = [[0 for _ in range(M)] for _ in range(N)]
        threewall(q)

    elif n < r :
        return
    else:
        T[r-1] = zero[n-1]
        comb(n-1, r-1, q)
        comb(n-1, r, q)





N,M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

max_safe = 0
zero = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            zero.append([i,j])

T = [0]*3

comb(len(zero),3,3)

print(max_safe)