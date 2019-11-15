import sys

sys.stdin = open('파스칼의 삼각형.txt')

T = int(input())

def pascal(n):
    p = [1]
    if n == 2:
        p.append(1)
    elif n > 2:
        for i in range(2, n):
            t = pascal(n - 1)
            p.append(t[i - 2] + t[i - 1])
        p.append(1)
    return p

for tc in range(T):
    N = int(input())
    n = 1
    print('#{}'.format(tc + 1))
    while n <= N:
        q = pascal(n)
        for i in q:
            print(i, end=' ')
        print()
        n += 1