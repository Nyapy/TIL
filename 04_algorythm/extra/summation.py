import sys

sys.stdin = open('summation.txt')

T = int(input())

for tc in range(1,1+T):
    arr = list(map(int, input().split()))
    min_s = arr[0]
    max_s = 0

    for i in range(len(arr)):
        a = arr[i]
        su = 0
        while a != 0:
            n = a % 10
            su += n
            a //= 10
        if su > max_s:
            max_s = su
        if su < min_s:
            min_s = su


    print("#{} {} {}" .format(tc, max_s, min_s))
