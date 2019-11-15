import sys

sys.stdin = open('특별한 정렬_input.txt')

T = int(input())

for tc in range(T):
    N = int(input())

    num_list = list(map(int, input().split()))
    c = 0
    while c != len(num_list):
        num_max = c
        for j in range(c+1, len(num_list)):
            if num_list[num_max] < num_list[j]:
                num_max = j
        num_list[c], num_list[num_max] = num_list[num_max], num_list[c]
        c+=1

        if c == len(num_list):
            break

        num_min = c
        for k in range(c+1, len(num_list)):
            if num_list[num_min] > num_list[k]:
                num_min = k
        num_list[c], num_list[num_min] = num_list[num_min], num_list[c]
        c +=1

    print("#{} ".format(tc + 1), end='')
    for l in range(10):
        print("{}" .format(num_list[l]), end=' ')
    print()