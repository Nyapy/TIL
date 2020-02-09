import sys

sys.stdin = open('leddar_input.txt')

T = 10

for tc in range(1,T+1):
    Tc = int(input())

    leddar = [list(map(int, input().split())) for _ in range(100)]

    dx = [-1, 1, 0]
    dy = [0, 0, -1]

    x = 0
    y = 99

    for i in range(100):
        if leddar[99][i] == 2:
            x = i
            break

    while y > 0:
        if y == 99:
            leddar[y][x] = 3
            x = x + dx[2]
            y = y + dy[2]
        else:
            for a in range(3):
                x = x + dx[a]
                y = y + dy[a]
                if x >= 0 and y > 0 and x < 100 :
                    if leddar[y][x] == 1:
                        leddar[y][x] = 0
                        break



    print('#{} {}'.format(tc, x))


