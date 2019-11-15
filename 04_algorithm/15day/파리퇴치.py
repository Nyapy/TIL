import sys

sys.stdin = open('파리퇴치.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    fly = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_sum = 0
            for k in range(i,i+M):
                for l in range(j,j+M):
                    fly_sum += fly[k][l]

            if max_fly < fly_sum:
                max_fly = fly_sum


    print('#{} {}' .format(tc, max_fly))