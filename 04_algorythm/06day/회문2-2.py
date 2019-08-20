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
            for k in range(len(arr)-j):
                flag = 1
                flag2 = 1
                for l in range(k//2):
                    if arr[i][j+l] != arr[i][j+k-l-1]:
                        flag = 0

                    if arr[j+l][i] != arr[j+k-l-1][i]:
                        flag2 = 0
                if flag :
                    leng = k
                    if leng > max_leng :
                        max_leng = leng
                if flag2 :
                    leng2 = k
                    if leng2 > max_leng:
                        max_leng = leng2

    print('#{} {}' .format(TC, max_leng))