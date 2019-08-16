import sys
sys.stdin = open("달팽이 숫자_input.txt")
sys.stdout = open('달팽이 숫자_output.txt', 'w')

T = int(input())

for tc in range(T):
    N = int(input())
    num = 0
    arr = [[0 for _ in range(N)] for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    x = 0
    y = 0
    tx = 0
    ty = 0
    seq = 0

    while num < N**2 :
       num += 1
       x = tx
       y = ty
       arr[y][x] = num

       tx = x + dx[seq]
       ty = y + dy[seq]

       if tx < 0 or ty < 0  or tx == N or ty == N or arr[ty][tx] != 0:
           seq = (seq+1) % 4
           tx = x
           ty = y
           tx = x + dx[seq]
           ty = y + dy[seq]

    print("#{}".format(tc+1))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end= ' ')
        print()

