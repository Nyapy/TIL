import sys
import time
from time import strftime

start_time = time.time()


sys.stdin = open('병합정렬.txt')

T = int(input())

def merge_sort(a):
    if len(a) == 1:
        return a
    else:
        left = a[:len(a)//2]
        right = a[len(a)//2:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

def merge(left, right):
    global cnt
    result =list()


    if left[-1] > right[-1]:
        cnt += 1

    l,r = 0, 0
    while l < len(left) or r < len(right):
        if l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        elif r >= len(right):
            result.append(left[l])
            l += 1
        elif l >= len(left):
            result.append(right[r])
            r += 1

    # while len(left) > 0 or len(right) > 0:
    #     if len(left) > 0 and len(right) > 0:
    #         if left[0] <= right[0]:
    #             result.append(left.pop(0))
    #         else:
    #             result.append(right.pop(0))
    #     elif len(left) > 0:
    #         result.append(left.pop(0))
    #
    #     elif len(right) > 0:
    #         result.append(right.pop(0))

    return result

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    print('#{} {} {}' .format(tc, merge_sort(arr)[len(arr)//2], cnt))
print(time.time() - start_time, 'seconds')