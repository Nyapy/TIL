import sys
sys.stdin = open('숫자 배열 회전.txt')

T = int(input())

def rot90(arr):
    trans = []
    for i in range(N):
        tem = []
        for j in range(N-1,-1,-1):
            tem += [arr[j][i]]

        trans.append(tem)

    return trans


for tc in range(1,1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    a1 = rot90(arr)
    a2 = rot90(a1)
    a3 = rot90(a2)

    print('#{}' .format(tc))
    for i in range(N):
        for j in range(N):
            print(a1[i][j], end = '')
        print(' ', end='')
        for j in range(N):
            print(a2[i][j], end = '')
        print(' ', end='')
        for j in range(N):
            print(a3[i][j], end = '')
        print()





