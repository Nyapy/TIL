import sys

sys.stdin = open('최대상금.txt')

T = int(input())

for tc in range(1,1+T):
    number, trade = input().split()

    number = list(map(int, number))
    trade = int(trade)

    a = 0
    idx = 0
    val = -1
    max_val = 0

    while trade > 0:
        val = -1
        for j in range(len(number)-1, a-1, -1):
            if number[j] > val :
                idx = j
                val = number[j]

        if idx != a:
            number[a], number[idx] = number[idx],number[a]
            a += 1

        elif idx == a:
            a += 1
            continue
        trade -=1

    print(number)