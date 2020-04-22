import sys

sys.stdin= open('A.txt')

def x(n):
    k = 0
    tem = 0
    while 1:
        tem = tem + (2**k)
        if k !=0 and n%tem ==0:
            break
        k+=1
    ks = 0
    for i in range(k+1):
        ks += 2**i

    return n//ks
T = int(input())


for tc in range(1,1+T):
    n = int(input())
    print(x(n))
