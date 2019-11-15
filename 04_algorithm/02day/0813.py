import sys

sys.stdin = open("0813_input.txt")

T = 10

for tc in range(T):

    N = int(input())
    arr = list(map(int, input().split()))


    for i in range(N):
        min = arr[0]
        min_num = 0
        max = arr[0]
        max_num = 0
        for j in range(len(arr)):
            if max < arr[j]:
                max = arr[j]
                max_num = j
            if min > arr[j]:
                min = arr[j]
                min_num = j
            # print(max_num, min_num)

        arr[max_num] = max-1
        arr[min_num] = min+1

        # print(max, max_num)
        # print(min, min_num)

    min = arr[0]
    min_num = 0
    max = arr[0]
    max_num = 0
    for k in range(len(arr)):
        if max < arr[k]:
            max = arr[k]
            max_num = k
        if min > arr[k]:
            min = arr[k]
            min_num = k

    print ("#{} {}".format(tc+1, max-min))