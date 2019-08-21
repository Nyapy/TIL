import sys

sys.stdin = open('백만장자.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    total = 0

    # for i in range(N) :
    #     max_price = 0
    #     benepit = 0
    #     for j in range(N-i):
    #         if price[i] < price[i+j]:
    #             benepit = price[i+j] - price[i]
    #         if benepit > max_price:
    #             max_price = benepit
    #
    #     total += max_price

    # for i in range(N) :
    #     max_price = 0
    #
    #     ace = max(price[i:N])
    #     if ace > price[i]:
    #         max_price = ace - price[i]
    #     total += max_price
    max_price = price[-1]

    for i in range(N):
        if price[N-i-1] < max_price:
            total += max_price-price[N-i-1]
        elif price[N-i-1] > max_price:
            max_price = price[N-i-1]


    print("#{} {}" .format(tc, total))