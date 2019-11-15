import sys

sys.stdin = open('수영장.txt')

T = int(input())

def daily(n, k, m3):
    global mt

    if m3 >= mt:
        return

    if k >= 12:
        total = 0
        a= 0

        B= [0]*14
        for j in range(12):
            if A[j] == 0:
                B[j] = 1

        for k in range(12):
            if B[k] == 1:
                a = tax[0]*month[k]

                if a > tax[1]:
                    a = tax[1]

            else:
                continue
            total += a

        total += m3

        if mt > total:
            mt = total



    else:
        if m3 < mt:
            for i in range(k,12):
                if A[i] == 0:
                    A[i] = 1
                    A[i+1] = 1
                    A[i+2] = 1
                    daily(12, k+3, m3+tax[2])
                    A[i] = 0
                    A[i+1] = 0
                    A[i+2] = 0
                    daily(12, k + 3, m3)






for tc in range(1,T+1):
    tax = list(map(int, input().split()))

    month = list(map(int, input().split()))

    how = list(range(1,15))
    total = 0
    mt = 11111111111111

    dal = tax[3]

    A =[0]*14

    daily(12, 0, 0)

    if mt > dal:
        mt = dal

    print('#{} {}' .format(tc, mt))