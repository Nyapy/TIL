import sys

sys.stdin = open('최대상금.txt')

T = int(input())

def prize(trade, number, cnt):
    a = number[:]

    for i in range(len(memo[cnt])):
        if memo[cnt][i] != 0:
            if memo[cnt][i] == a:
                return
        elif memo[cnt][i] == 0:
            memo[cnt][i] = a
            break

    if trade == 0:
        return

    for i in range(len(number)):
        for j in range(i+1, len(number)):
            number[i], number[j] = number[j], number[i]
            prize(trade-1 , number, cnt+1)
            number[i], number[j] = number[j], number[i]

def fact(n):
    a = 1
    while n > 0:
        a *= n
        n -= 1
    return a

for tc in range(1,1+T):
    number, trade = input().split()
    ans = []
    cnt = 0

    number = list(map(int, number))
    trade = int(trade)
    fa = fact(len(number))


    memo =[[0 for _ in range(fa)] for __ in range(trade+1)]
    prize(trade, number, cnt)
    # print(memo)

    ans = memo[trade][:]
    real = []

    for i in ans:
        if i == 0:
            1
        else:
            real.append(i)

    real.sort(reverse=1)


    print('#{}' .format(tc) , end = ' ')
    for i in real[0]:
        print(i, end = '')
    print()
