import sys

sys.stdin = open('종이붙이기_input.txt')

T = int(input())

def fac(n):
    mul = 1
    for i in range(1,n+1):
        mul *= i
    return mul

for tc in range(1, T+1):
    N = int(input())
    w1 = 10
    w2 = 20
    cnt = 0
    for i in range(0,(N//w1)+1):
        for j in range(0, (N//w2)+1):
            if i*w1+j*w2 == N:
                cnt += int(fac(i+j)/(fac(i)*fac(j))*(2**j))

    print('#{} {}' .format(tc, cnt))