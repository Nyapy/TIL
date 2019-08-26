import sys

sys.stdin = open('계산기3.txt')

T = 10

first = {'(' : 1, '*' : 3, '/': 3, '+':2, '-':2}
operation = '(+-/*)'
numbers = '1234567890'

for tc in range(T):
    cer_len = int(input())
    ceremony = input()
    oper = []
    calculation = []
    a = '#'
    tem = []
    stack = []

    f = 0
    g = 0
    tem = 0

    for i in ceremony:
        if i in operation :
            if i =='(':
                oper.append(i)

            elif i == ')':
                while oper[-1] != '(':
                    a = oper.pop()
                    if a != '(':
                        calculation.append(a)
                oper.pop()

            else:
                while first.get(oper[-1]) >= first.get(i):
                    b = oper.pop()
                    calculation.append(b)

                if first.get(oper[-1]) < first.get(i):
                    oper.append(i)
        else:
            calculation.append(i)

    # while oper != []:
    #     a= oper.pop()
    #     if a != '(':
    #         calculation.append(a)


    # print(''.join(calculation))

    for i in calculation:
        if i in numbers:
            stack.append(int(i))
        else:
            f = stack.pop()
            g = stack.pop()
            if i == '+':
                tem = g + f
            if i == '-':
                tem = g + f
            if i == '*':
                tem = g * f
            if i == '/':
                tem = g/f
            stack.append(tem)

    print('#{} {}'.format(tc+1, stack.pop()))
