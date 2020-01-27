import sys

sys.stdin = open("1713.txt")
N = int(input())
M = int(input())
data = list(map(int, input().split()))
time = 0
recommend = [[0, 0, 0] * N for _ in range(N)]
min_rec = 1 << 30
for i in data:
    for j in range(N):
        if recommend[j][2] == i:
            recommend[j][0] += 1
            break
    else:
        recommend.sort()
        recommend[0] = [1, time, i]
        time += 1
ans = [k[2] for k in recommend]
ans.sort()
print(' '.join(map(str, ans)))