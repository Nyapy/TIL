import sys
sys.stdin = open('d.txt')

N = int(input())

arr = list(map(int, input().split()))

print(arr)


far_dist = 0

for i in range(len(arr)):
    dist = 20000
    min_dis = 20000
    if arr[i] == 0:
        if i == 0:
            for j in range(i+1, len(arr)):
                if arr[j] == 1:
                    dist = j - i
                break
            if min_dis > dist:
                min_dis = dist

        elif i == len(arr)-1:
            for j in range(i):
                if arr[j] == 1:
                    dist = i - j
            if min_dis > dist:
                min_dis = dist

        else:
            for j in range(i):
                if arr[j] == 1:
                    dist = i - j

            for j in range(i + 1, len(arr)):
                if arr[j] == 1:
                    dist2 = j - i
                    break
            if min_dis > dist:
                min_dis = dist
            if min_dis > dist2:
                min_dis = dist2

    else:
        continue

    if min_dis > far_dist:
        far_dist = min_dis

print(far_dist)