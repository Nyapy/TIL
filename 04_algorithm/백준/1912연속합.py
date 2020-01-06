import sys

sys.stdin = open("1912연속합.txt")

n = int(input())

numbers = list(map(int, input().split()))

result = n * -1000

for i in range(1,n+1):
    for j in range(n+1 - i):
        ans = 0
        for k in range(j, j+i):
            ans += numbers[k]
        if ans > result :
            result = ans

print(result)