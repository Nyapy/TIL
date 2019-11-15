import sys

sys.stdin = open('0814.txt')

T = 10
for tc in range(T):
    sum_li = []
    tcn = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_lcross = 0
    sum_rcross = 0

    for i in range(100):
        sum_row = 0
        sum_col = 0
        for j in range(100):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
            if i == j:
                sum_lcross += arr[i][j]
            if i+j == 99:
                sum_rcross += arr[i][j]

        sum_li.append(sum_row)
        sum_li.append(sum_col)
    sum_li.append(sum_lcross)
    sum_li.append(sum_rcross)


    max_val = sum_li[0]

    for a in range(len(sum_li)):
        if sum_li[a] >= max_val:
            max_val = sum_li[a]

    print("#{} {}" .format(tcn, max_val))
