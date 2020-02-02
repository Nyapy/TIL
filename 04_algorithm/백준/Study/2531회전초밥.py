import sys
sys.stdin = open("2531.txt")

N, d, k, c = map(int, input().split())
susi = [int(input()) for _ in range(N)]
candi = []
check = [0]*(d+1)

start = 0
end = 0+k

cnt =0
for a in range(start, end):
    if check[susi[a]] == 0:
        cnt += 1
    check[susi[a]] += 1

result = 0
if result < cnt:
    result = cnt
    if check[c] == 0:
        result += 1

while start < N:

    if result == k+1:
        break

    if check[susi[start]] == 1:
        cnt -= 1

    check[susi[start]] -= 1

    if check[susi[end]] == 0:
        cnt +=1

    check[susi[end]] += 1

    if result <= cnt :
        result = cnt
        if check[c] == 0:
            result += 1

    start += 1
    end = (end+1)%N


print(result)
