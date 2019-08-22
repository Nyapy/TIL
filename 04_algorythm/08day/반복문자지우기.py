import sys

sys.stdin = open('반복문자지우기_input.txt')

T = int(input())

for tc in range(T):
    s = input()
    s_li = list(s)

    cnt = 1


    for i in range(len(s)//2):
        for j in range(0, len(s_li)-1) :
            if s_li[j] == s_li[j+1]:
                s_li[j] =0
                s_li[j+1] =0

        cnt = s_li.count(0)
        for _ in range(cnt):
            s_li.remove(0)

    print('#{} {}' .format(tc+1, len(''.join(s_li))))