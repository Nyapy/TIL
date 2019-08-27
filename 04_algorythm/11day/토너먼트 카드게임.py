import sys

sys.stdin = open('토너먼트 카드게임.txt')

T = int(input())

def RSP(a,b):
    if a == 1 and b == 2:
        return b
    elif a == 1 and b == 3:
        return a
    elif a == 2 and b == 1 :
        return a
    elif a == 2 and b == 3:
        return a
    elif a == 3 and b == 1 :
        return b
    elif a == 3 and b == 2 :
        return b
    else :
        return

def winner(a):
        if len(a) == 2:
            return RSP(a[0],a[1])

        elif len(a) == 1:
            return a[0]

        elif len(a)% 2 == 0:
            A = winner(a[:len(a)//2])
            B = winner(a[(len(a)//2):])
            # print(A, B)
            return RSP(A,B)

        elif len(a)%2 == 1 :
            A = winner(a[:len(a)//2+1])
            B = winner(a[len(a)//2+1:])
            # print(A, B)
            return RSP(A,B)

for tc in range(T):

    N = int(input())

    rsp = list(map(int, input().split()))
    RSP = dict()
    for i in range(len(rsp)):
        RSP[i+1] = rsp[i]

    print(RSP)
    # print(winner(rsp))
