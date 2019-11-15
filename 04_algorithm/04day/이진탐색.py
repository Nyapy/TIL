import sys

sys.stdin = open('이진탐색_input.txt')

T = int(input())

def binary(x, P):
    cnt = 0
    l = 1
    r = P
    m = 0
    while m != x:
        m = int((l + r) / 2)

        if m > x:
            r = m
        else:
            l = m
        cnt += 1
    return cnt


for tc in range(1, T+1):
    P, A, B = map(int, input().split())


    cnt_a = binary(A, P)
    cnt_b = binary(B, P)

    if cnt_a > cnt_b :
        print('#{} B' .format(tc))
    elif cnt_a < cnt_b :
        print('#{} A' .format(tc))
    elif cnt_a == cnt_b :
        print('#{} 0' .format(tc))