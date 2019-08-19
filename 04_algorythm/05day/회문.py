import sys

sys.stdin = open('회문_input.txt')

T = 10

for tc in range(T):
    length = int(input())
    numbers = []
    cnt = 0
    for i in range(8):
        numbers += input().split()

    # numbers = [input().split() for _ in range(8)]

    for a in range(8):
        for i in range(8 -length +1):
            palin_r = ''
            palin_c = ''
            for j in range(length):
                palin_r += numbers[a][i+j]
                palin_c += numbers[i+j][a]

            if palin_r == palin_r[::-1]:
                cnt += 1
            if palin_c == palin_c[::-1]:
                cnt += 1

    print('#{} {}' .format(tc+1, cnt))
