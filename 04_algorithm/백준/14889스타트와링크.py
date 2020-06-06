import sys

sys.stdin = open("14889.txt")

N = int(input())

con= 1
jet = 1
for i in range(N,N//2,-1):
    con *= i
for j in range(1,N//2+1):
    jet *= j

conn = con//jet

cnt = 0
S = [list(map(int, input().split())) for _ in range(N)]
team = list(range(N))

ans = 100 *N**2

start = [0]* (N//2)
a = []
b = []
def comb(n,k,q):
    global ans, cnt
    if cnt == conn:
        return
    if N-k < n-q:
        return
    if n == q :
        cnt += 1
        link = []
        for i in team:
            if i not in start:
                link.append(i)
        score = 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                score += S[start[i]][start[j]]+S[start[j]][start[i]]

        for i in range(N//2):
            for j in range(i+1, N//2):
                score -= (S[link[i]][link[j]] + S[link[j]][link[i]])

        if ans > abs(score):
            ans = abs(score)

        return

    else:
        start[q] = team[k]
        comb(n, k + 1, q + 1)
        start[q] = 0
        comb(n,k+1,q)

comb(N//2, 0, 0)

print(ans)
