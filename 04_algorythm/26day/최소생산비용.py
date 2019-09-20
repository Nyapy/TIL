import sys

sys.stdin = open('최소생산비용.txt')

T = int(input())

def perm(n,k, s):
    global minprice
    if n == k :
        if s < minprice:
            minprice = s

    else :
        if minprice > s:
            for i in range(k, n):
                prod[i], prod[k] = prod[k], prod[i]
                perm(n,k+1,s+plant[k][prod[k]])
                prod[i], prod[k] = prod[k], prod[i]


for tc in range(1,1+T):
    N = int(input())
    plant = [list(map(int,input().split())) for _ in range(N)]
    minprice = 15*99
    prod = [i for i in range(N)]

    perm(N, 0, 0)

    print('#{} {}' .format(tc, minprice))