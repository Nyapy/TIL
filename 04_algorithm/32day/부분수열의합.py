import sys

sys.stdin = open('부분수열의합.txt')

T = int(input())


def bubun(n,k, s):
    global cnt

    if s > K:
        return

    if n == k:
        if s == K:
            cnt += 1

    else:
        A[k] = 1
        bubun(n,k+1, s+arr[k])
        A[k] = 0
        bubun(n, k+1, s)

for tc in range(1, 1+T):


    N, K = map(int, input().split())
    A = [0]*N
    cnt = 0
    arr = list(map(int, input().split()))

    bubun(N,0,0)

    print("#{} {}" .format(tc, cnt))