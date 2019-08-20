import sys

sys.stdin = open('회문2_input.txt')

T = 10

for tc in range(T):
    TC = input()
    arr = []
    max_leng = 0

    for a in range(100):
        arr += input().split()

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            check_row = ''
            check_col = ''
            leng_r = 0
            leng_c = 0
            for k in range(len(arr)-j):
                check_row += arr[i][j+k]
                check_col += arr[j+k][i]
                if check_row == check_row[::-1]:
                    leng_r = len(check_row)
                if check_col == check_col[::-1]:
                    leng_c = len(check_col)
                if leng_r > leng_c:
                    leng = leng_r
                else:
                    leng = leng_c
                if leng > max_leng:
                    max_leng = leng



    print('#{} {}' .format(TC, max_leng))