import sys

sys.stdin = open('수의 새로운 연산.txt')

T = int(input())

def location(n):
    total = 0
    x=0
    i = 1
    while total < n:
        total += i
        x = i
        i += 1
    y = n - total + x
    return y, x-y+1

def num(x,y) :
    a = x + y -1
    n = 0
    for i in range(a):
        n+=i
    return n+x

for tc in range(T):
    q, p = map(int, input().split())

    # print(location(8))

    lo_q = location(q)
    lo_p = location(p)

    lo_x = lo_q[0] + lo_p[0]
    lo_y = lo_q[1] + lo_p[1]

    print('#{} {}' .format(tc+1, num(lo_x, lo_y)))

