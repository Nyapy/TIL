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

    for j in range(len(num)):
        if j ==0:
            print(TC)
        for k in range(arr_dic[num[j]]):
            print(num[j], end = ' ')
    print()