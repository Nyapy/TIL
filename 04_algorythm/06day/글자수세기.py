import sys

sys.stdin = open('글자수세기_input.txt')

T = int(input())

for tc in range(T):
    str1 = input()
    str2 = input()

    str1 = set(str1)
    max = 0

    for i in str1:
        count = 0

        for j in str2:
            if i == j:
                count +=1
        if count > max:
            max = count

    print('#{} {}' .format(tc+1, max))