def partition(a, l, r):
    pivot = a[l]
    i, j = l, r

    while i < j:
        while a[i] <= pivot:
            i += 1
            if(i == r): break
        while a[j] >= pivot :
            j -= 1
            if(j == l): break
        if i < j :
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def quicksort(a, l, r):
    if l < r:
        pivot = partition(a, l, r)
        quicksort(a, l, pivot-1)
        quicksort(a, pivot+1, r)

import sys
sys.stdin = open('(5205)퀵정렬_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    quicksort(A, 0, N-1)
    print('#{} {}'.format(tc, A[N//2]))

