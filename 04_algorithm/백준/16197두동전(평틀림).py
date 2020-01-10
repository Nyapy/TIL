import sys
sys.stdin = open('16197두동전.txt')
N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
coin = []
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 'o':
            coin.append([y, x])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
arr = []
ans = -1
def solve(arr):
    global ans
    coin_tmp = [coin[0][:] , coin[1][:]]
    for i in arr:
        flag = 0
        for j in coin_tmp:
            ty = j[0] + dy[i]
            tx = j[1] + dx[i]
            if 0 > ty or N <= ty or 0 > tx or M <= tx:
                flag += 1
            elif MAP[ty][tx] != '#':
                j[0], j[1] = ty, tx
        if flag == 1:
            return len(arr)
        if flag == 2:
            return -1
    return -1
def d(n, a):
    global ans
    if n == a+1:
        return
    if n > 10:
        return
    if n > 1 and ans == -1:
        ans = solve(arr)
    if ans != -1:
        return
    for i in range(4):
       arr.append(i)
       d(n+1, a)
       arr.pop()
for i in range(1, 11):
    d(1, i)
    if ans != -1:
        break
print(ans)