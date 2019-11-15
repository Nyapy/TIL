import sys
sys.stdin = open("달팽이 숫자_input.txt")

T = int(input())

for tc in range(T):
    N = int(input())

    arr = [[0 for _ in range(N)] for _ in range(N)]

    j = [2]*(N-2)
    j.insert(0,3)
    # print(j)

    col = 0
    dr = N
    row = 0
    ul = 0
    num = 1
    rot=(2*N-1)


    for a in range(rot):

        if a % 4 == 0 :
            while col < dr:
                arr[row][col] = num
                col += 1
                num += 1
            col -= 1
            num -= 1

        if a % 4 == 1 :
            while row < dr:
                arr[row][col] = num
                row += 1
                num += 1
            row -= 1
            num -= 1


        if a % 4 == 2 :
            while col >= ul:
                arr[row][col] = num
                col -= 1
                num += 1
            col +=1
            num -= 1
            dr -= 1


        if a % 4 == 3 :
            while row > ul:
                arr[row][col] = num
                row -= 1
                num += 1
            row += 1
            num -= 1
            ul += 1


    print('#{}'.format(tc+1))
    for q in range(N):
        for w in range(N):
            print(arr[q][w], end = ' ')
        print()

