import sys

sys.stdin = open('forth.txt')

T = int(input())

oper = '+-/*.'

def cal(fom):
    for i in fom:
        if i not in oper:
            stack.append(int(i))

        else:
            if len(stack) >= 2:
                if i != '.':
                    f = stack.pop()
                    g = stack.pop()
                    if i == '+':
                        tem = f+g
                    elif i == '-' :
                        tem = g-f
                    elif i == '*':
                        tem = f*g
                    elif i == '/':
                        tem = g//f

                else :
                    return print('#{} error'.format(tc + 1))


                stack.append(tem)

            elif len(stack)==1:
                if i == '.':
                    return print('#{} {}' .format(tc+1, stack.pop()))
                else :
                    return print('#{} error' .format(tc+1))

            else :
                return print('#{} error' .format(tc+1))



for tc in range(T):
    stack = []
    fom = list(input().split())

    # print(fom)

    cal(fom)

