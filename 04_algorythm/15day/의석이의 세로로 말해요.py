import sys

sys.stdin = open('의석이의 세로로 말해요.txt')

T = int(input())

for tc in range(1,T+1):
    mal = [list(input()) for _ in range(5)]

    leng = 0
    for i in mal:
        if leng < len(i):
            leng = len(i)

    mal2 = [[0 for _ in range(leng)] for __ in range(5)]

    for i in range(len(mal)):
        for j in range(len(mal[i])):
            mal2[i][j] = mal[i][j]

    ans = []

    for i in range(len(mal2[0])):
        for j in range(len(mal2)):
            if mal2[j][i] != 0:
                ans += [mal2[j][i]]


    print('#{} {}' .format(tc, ''.join(ans)))