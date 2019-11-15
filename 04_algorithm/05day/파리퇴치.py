import sys
sys.stdin = open("파리퇴치_input.txt")

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0


    for a in range(len(arr)-M+1):
        for b in range(len(arr) - M + 1):
            tem = 0
            for c in range(M):
                for d in range(M):
                    tem += arr[a+c][b+d]

            if tem > max_fly:
                max_fly = tem

    print('#{} {}'.format(tc+1, max_fly))