import sys

sys.stdin = open('이진수2.txt')

T = int(input())

def biprint(n):
    a = ''
    bi = []
    while n != 0:
        n = n * 2

        if n >= 1:
            n -= 1
            bi.append(1)
        elif n < 1:
            bi.append(0)
        if len(bi) >= 13:
            return 'overflow'

    for i in bi:
        a += str(i)
    return a

for tc in range(1,T+1):
    n = float(input())
    biprint(n)
    print('#{} {}' .format(tc, biprint(n)))
