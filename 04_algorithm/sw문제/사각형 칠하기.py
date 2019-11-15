import sys

sys.stdin = open('사각형 칠하기.txt')

T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split())
    color = [list(map(int, input().split())) for _ in range(K)]
    count = 0
    max_count = 0
    zero = 0

    paint = [[0 for _ in range(M)] for __ in range(N)]
    # print(color)

    for c in color:
        cola = 0
        for i in range(c[0],c[2]+1):
            for j in range(c[1], c[3]+1):
                if paint[i][j] > c[4]:
                    cola = 1
        if cola == 0:
            for i in range(c[0], c[2] + 1):
                for j in range(c[1], c[3] + 1):
                    paint[i][j] = c[4]


    for c in range(12):
        count = 0
        zero = 0
        for i in range(N):
            for j in range(M):
                if paint[i][j] == c:
                    count += 1

        if max_count < count :
            max_count = count

    print('#{} {}' .format(tc+1, max_count))