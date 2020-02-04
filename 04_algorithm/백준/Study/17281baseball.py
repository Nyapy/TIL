import sys

sys.stdin = open("17281.txt")

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

seq = list(range(1,10))

def com(k, n):
    if k == n:
        1
    else:
        arr[k], arr[i] = arr[i], arr[]