import sys

sys.stdin = open("15684.txt")

N, M, H = map(int , input().split())

garo = [list(map(int, input().split())) for _ in range(M)]

letter = [[0 for _ in range(N)] for _ in range(H+1)]
ans = -1
candi = []

for info in garo:
    a,b = info
    letter[a][b] = 1

for i in range(1,H+1):
    for j in range(1, N):
        if letter[i][j]==0:
            candi.append([j,i])
def comb(n,k,q, se):
    global ans
    if ans >= 0:
        return
    if n-k < se -q :
        return
    if q == se:
        flag = 1
        for x in range(1,N+1):
            done = game(x)
            if not done :
                flag = 0
                break
        if flag:
            ans = se

        return

    else:
        x,y = candi[k]
        flag = 0
        if x-1 >= 0:
            if letter[y][x-1]:
                flag += 1
        if x < N:
            if letter[y][x]:
                flag += 1

        if flag >= 1:
            comb(n,k+1,q,se)
        else:
            comb(n, k + 1, q, se)
            letter[y][x] =1
            comb(n,k+1,q+1,se)
            letter[y][x] = 0

def game(x):
    sero = 1
    nx = x
    while sero < H:
        for k in [-1,0]:
            tx = nx+k
            if 1 <= tx < N:
                if letter[sero][tx] == 1:
                    if k == -1:
                        nx = tx
                        break
                    elif k == 0:
                        nx = tx+1
        sero += 1
    if nx == x:
        return True
    else :
        return False


for i in range(4):
    comb(len(candi),0,0,i)
    if ans >= 0:
        break

print(ans)
# for i in range(1,M+1):
#     game(i)