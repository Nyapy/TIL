import sys
sys.stdin = open('prac2.txt')


arr = list(map(int, input().split()))
for i in range(1, 1 << len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i & (1 << j):
            sum += arr[j]



    if sum == 10:
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end= ' ')
        print()

