import sys
sys.stdin = open("달팽이 숫자_input.txt")

T = int(input())

for tc in range(T):
    N = int(input())

    arr = [[0 for _ in range(N)] for _ in range(N)]

    col = 0
    col_n = N
    row = 0
    row_n = 0
    num = 1
    rot=(2*N-1)


    for a in range(rot):
        if a % 4 == 0 :
            while col < col_n:
                arr[row][col] = num
                col += 1
                num += 1
            col -= 1
            num -= 1

        if a % 4 == 1 :
            while row < col_n:
                arr[row][col] = num
                row += 1
                num += 1
            row -= 1
            num -= 1

        if a % 4 == 2 :
            while col > row_n:
                arr[row][col] = num
                col -= 1
                num += 1
            col +=1
            col_n -=1
            num -= 1

        if a % 4 == 3 :
            while row > row_n:
                arr[row][col] = num
                row -= 1
                num += 1
            row += 1
            row_n -=1
            num -= 1

    for q in range(N):
        for w in range(N):
            print(arr[q][w], end = ' ')
        print()

