import sys

sys.stdin = open('Magnetic.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for i in range(N):
        isN = 0
        for j in range(N):
            if table[j][i] == 1:
                isN= 1

            elif table[j][i] ==2 and isN == 1:
                cnt += 1
                isN = 0

    print('#{} {}' .format(tc, cnt))