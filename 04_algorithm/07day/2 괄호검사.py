
def parenthesis(a):
    check = []
    for i in range(len(a)):
        if a[i] == '(':
            check.append(a[i])
        elif a[i] == ')':
            if check == []:
                return print('괄호 ㄴ')
            else :
                check.pop()

    if len(check) == 0 :
        print('괄호 잘됨')

    else :
        print('괄호 ㄴㄴ')

q = input()

parenthesis(q)