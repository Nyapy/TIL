import sys

sys.stdin = open('괄호검사_input.txt')

T = int(input())

def paren(a):
    pa_list = list()
    for i in range(len(a)):
        c = a[i]
        if a[i] == '{' or a[i] == '(' :
            pa_list.append(a[i])

        elif a[i] == '}':
            if len(pa_list) != 0 :
                tem = pa_list.pop()
                if tem != '{':
                    return 0
            else :
                return 0

        elif a[i] == ')':
            if len(pa_list) != 0 :
                tem = pa_list.pop()
                if tem != '(':
                    return 0
            else :
                return 0

    if len(pa_list) == 0:
        return 1
    else :
        return 0


for tc in range(T):

    a= input()

    print('#{} {}'.format(tc+1, paren(a)))