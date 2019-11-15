import sys

sys.stdin = open('문자열비교_input.txt')

def palin(str1, str2):

    for i in range(len(str2)-len(str1)+ 1):
        count = 0
        for j in range(len(str1)):
            if str2[i + j] == str1[j]:
                count += 1
            if count == len(str1):
                return 1

    return 0

T = int(input())


for tc in range(T):
    str1 = input()
    str2 = input()

    A = palin(str1, str2)

    print('#{} {}' .format(tc+1, A))

