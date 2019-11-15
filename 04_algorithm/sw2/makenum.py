import sys

sys.stdin = open('makenum.txt')

T = int(input())

def cal(oper):
    global maxnum, minnum

    A = numbers[0]
    seq = 1
    for i in range(len(oper)):
        if oper[i] == 0:
            A += numbers[seq]

        elif oper[i] == 1:
            A -= numbers[seq]

        elif oper[i] == 2:
            A *= numbers[seq]

        else:
            A /= numbers[seq]
            A =int(A)
        seq+=1
    if A > maxnum:
        maxnum=A

    if A < minnum:
        minnum = A
    print(A)
def perm(n, k):
    if n == k :
        cal(oper)

    else:
        for i in range(k, n):
            oper[i],oper[k] = oper[k],oper[i]
            perm(n, k+1)
            oper[i], oper[k] = oper[k], oper[i]

for tc in range(T):
    N = int(input())
    tem = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    oper = []
    for i in range(4):
        oper += [i]*tem[i]

    maxnum = -100000000
    minnum = 100000000
    # 0: + , 1:-, 2:*, 3:/



    perm(len(oper), 0)

    print('#{} {}' .format(tc+1, maxnum-minnum))