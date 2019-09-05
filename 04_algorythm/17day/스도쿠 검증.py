import sys

sys.stdin = open('스도쿠 검증.txt')

def check():
    for i in range(9):
        row = []
        col = []
        can = []
        for j in range(9):
            row += [sdoku[i][j]]
            col += [sdoku[j][i]]

            if i % 3 == 0 and j % 3 == 0:
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        can +=[sdoku[k][l]]
            if len(can) == 9:
                can.sort()
                if can != sort:
                    return 0
                can = []
        row.sort()
        col.sort()
        if row != sort or col != sort :
            return 0

    return 1


T= int(input())
for tc in range(1,1+T):

    sort = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    sdoku = [list(map(int, input().split())) for _ in range(9)]

    print("#{} {}" .format(tc, check()))




