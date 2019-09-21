import sys

sys.stdin = open('이진 탐색.txt')

T = int(input())

def binary(a):
    global cnt
    l = 0
    r = len(A)-1
    m = (l+r)//2
    flag = 2

    while l <= r:
        if A[m] == a:
            cnt += 1
            return
        if l == r :
            if A[m] != a:
                break

        if A[m] > a:
            if flag == 1:
                return
            r = m-1
            m = (l+r) // 2
            flag = 1

        else :
            if flag == 0:
                return
            l = m+1
            m = (l + r) // 2
            flag = 0
    return

for tc in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    A=sorted(A)
    for a in B:
        binary(a)

    print('#{} {}' .format(tc, cnt))