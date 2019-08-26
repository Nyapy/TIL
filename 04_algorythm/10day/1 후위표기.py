#
# woosun =  if
#
# plmi = ['+', '-']
# muldi = ['*', '/']
# par = ['(', ')']
#
#
c ='2+3*4/5'
#
# oper = []
# calculattion = []
#
# for i in c :
#     if i == '(' :
#         oper.append(i)
#     if i in plmi :
#         if oper == []:
#             oper.append(i)
#         if oper != []:
#             oper[-1]

str = '2+3*4/5'
stack = []

for i in range(len(c)):
    if str[i] == '+' or str[i] =='-' or str[i] == '*' or str[i] == '/':
        stack.append(str[i])

    else:
        print(str[i], end = "")

while len(stack) != 0:
    print(stack.pop(), end= "")