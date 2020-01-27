import sys

sys.stdin = open("10844.txt")

N = int(input())

chart = [[0 for _ in range(10)] for _ in range(N+1)]

for i in range(1,10):
    chart[1][i] = 1
n = 2
while n <= N:
    for i in range(10):
        if i == 0:
            chart[n][i] = chart[n-1][i+1]
        elif i == 9:
            chart[n][i] = chart[n-1][i-1]
        else:
            chart[n][i] = chart[n-1][i+1]+chart[n-1][i-1]
    n+=1
result = 0
for i in range(10):
    result += chart[N][i]
print(result%1000000000)