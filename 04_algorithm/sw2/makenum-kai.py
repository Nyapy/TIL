import sys

sys.stdin = open('makenum.txt')

T = int(input())

def cal(num1, seq):
    global maxnum, minnum

    if seq == len(numbers):
        # print("nym: {}" .format(num1))
        if num1 > maxnum:
            maxnum = num1

        if num1 < minnum:
            minnum = num1
        return

    # print(num1)
    for k in range(4):
        if oper[k] != 0:
            oper[k] -= 1
            if k == 0:
                A = num1+numbers[seq]
            elif k == 1:
                A = num1 - numbers[seq]
            elif k == 2:
                A = num1 * numbers[seq]
            else:
                A = num1 / numbers[seq]
                A = int(A)
            cal(A, seq + 1)
            oper[k] += 1


for tc in range(T):
    N = int(input())
    oper = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    A = 0

    maxnum = -100000000
    minnum = 100000000
    # 0: + , 1:-, 2:*, 3:/

    cal(numbers[0], 1)

    print('#{} {}' .format(tc+1, maxnum-minnum))