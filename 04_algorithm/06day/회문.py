import sys

sys.stdin = open('회문_input.txt')

T = int(input())

for tc in range(T):
    N, length = map(int, input().split())
    numbers = []

    cnt = 0
    for i in range(N):
        numbers += input().split()

    for a in range(N):
        for i in range(N -length +1):
            palin_r = ''
            palin_c = ''
            for j in range(length):
                palin_r += numbers[a][i+j]
                palin_c += numbers[i+j][a]

            if palin_r == palin_r[::-1]:
                print('#{} {}' .format(tc+1, palin_r))
            if palin_c == palin_c[::-1]:
                print('#{} {}'.format(tc + 1, palin_c))
