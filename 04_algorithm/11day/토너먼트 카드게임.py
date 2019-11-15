import sys

sys.stdin = open('토너먼트 카드게임.txt')

T = int(input())

def RSP(a,b):
    if rsp[a] == 1 and rsp[b] == 2:
        return b
    elif rsp[a] == 1 and rsp[b] == 3:
        return a
    elif rsp[a] == 2 and rsp[b] == 1 :
        return a
    elif rsp[a] == 2 and rsp[b] == 3:
        return b
    elif rsp[a] == 3 and rsp[b] == 1 :
        return b
    elif rsp[a] == 3 and rsp[b] == 2 :
        return a
    elif rsp[a] == rsp[b]:
        return a

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
    index = []

    rsp = list(map(int, input().split()))
    for i in range(N):
        index += [i]

    A = winner(index)
    print('#{} {}' .format(tc+1, A+1))