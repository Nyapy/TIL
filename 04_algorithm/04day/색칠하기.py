import sys

sys.stdin = open('색칠하기_input.txt')

T = int(input())

for tc in range(1, T+1):
    count = 0

    cart = [[0 for _ in range(10)] for _ in range(10)]

    color_n = int(input())
    # print(color_n)
    info = [list(map(int, input().split())) for _ in range(color_n)]

    for i in info:
        for j in range(i[0],i[2]+1) :
            for k in range(i[1],i[3]+1):
                cart[j][k] += i[4]



    for i in range(len(cart)):
        for j in range(len(cart[i])):
            if cart[i][j] ==3:
                count += 1
        #     print(cart[i][j], end=' ')
        # print()

    print('#{} {}' .format(tc, count))


