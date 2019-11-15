import sys

sys.stdin = open('정곤이의 단조 증가하는 수.txt')

T = int(input())


# def dangjo():

def printset(n):
    a = 1
    for i in range(n):
        if bubun[i]:
            a *= Num[i]

    dangjo(a)


def dangjo(N):
    rest = 9
    a = N
    while a != 0:
        b = a % 10
        if b > rest:
            return
        rest = b
        a = a // 10

    candi.append(N)


def powerset(n, k, su):
    if n == k:
        if su == 2:
            printset(n)
    else:
        if su <= 2:
            bubun[k] = 1
            powerset(n, k + 1, su + 1)

            bubun[k] = 0
            powerset(n, k + 1, su)
        else :
            return


for tc in range(1, T + 1):
    N = int(input())
    Num = list(map(int, input().split()))
    bubun = [0] * N

    candi = [-1]

    powerset(N, 0, 0)

    print('#{} {}'.format(tc, max(candi)))