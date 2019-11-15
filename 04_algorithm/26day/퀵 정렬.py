import sys

sys.stdin = open('퀵 정렬.txt')

T = int(input())
def Hoare(A, l, r):
    p = A[l]
    i = l
    j = r
    while i < j:
        while A[i] <= p and i < r:
            i += 1
        while A[j] > p and j > l:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def HP(a, l, r):
    if l == r:
        return
    elif l < r:
        p = Hoare(a, l, r)
        HP(A, l, p - 1)
        HP(A, p + 1, r)

for tc in range(1,T+1):
    N = int(input())
    A = list(map(int, input().split()))
    r = len(A)-1
    l = 0
    HP(A,l, r)
    print('#{} {}' .format(tc, A[N//2]))