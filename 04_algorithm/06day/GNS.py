import sys

sys.stdin = open('GNS_input.txt')

T = int(input())

for tc in range(T):
    TC, N = input().split()

    N = int(N)

    arr = list(input().split())

    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    arr_dic = {}

    for i in num :
        arr_dic[i] = arr.count(i)

    arr =[]

    for j in num:
        for k in range(arr_dic[j]):
            arr.append(j)
    print(TC)
    for n in range(N):
        print(arr[n], end = ' ')
    print()
