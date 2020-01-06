import sys

sys.stdin = open("1912연속합.txt")

n = int(input())

numbers = list(map(int, input().split()))

result = numbers[0]
for i in range(n):
    if result <  numbers[i]:
        result = numbers[i]

a = 0
for i in range(n):
    a += numbers[i]
    if a < 0 :
        a = 0
    else:
        if a > result:
            result = a

print(result)