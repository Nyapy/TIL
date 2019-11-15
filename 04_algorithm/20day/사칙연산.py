import sys

sys.stdin = open('사칙연산.txt')

T= 10

def cal(a,b,c):
    if c == '+':
        dap = a+b
    elif c == '-':
        dap = a-b

    elif c == '*':
        dap = a*b
    elif c == '/':
        dap = a/b

    return dap

def postorder(t):
    if t != 0:
        if str(tree[t][3]).isdigit() == False :
            a = postorder(tree[t][0])
            b = postorder(tree[t][1])
            c = tree[t][3]
            return cal(a,b,c)
        elif str(tree[t][3]).isdigit():
            return tree[t][3]

for tc in range(1,1+T):
    N = int(input())
    info = [list(input().split()) for _ in range(N)]
    # print(info)

    tree = [[0]*4 for _ in range(N+1)]

    for i in range(len(info)):
        if len(info[i]) == 4:
            tree[int(info[i][0])][0] = int(info[i][2])
            tree[int(info[i][0])][1] = int(info[i][3])
            tree[int(info[i][0])][3] = info[i][1]

            tree[int(info[i][2])][2] = info[i][0]
            tree[int(info[i][3])][2] = info[i][0]
        elif len(info[i]) == 2:
            tree[int(info[i][0])][3] = int(info[i][1])

    # for i in range(N+1):
    #     for j in range(4):
    #         print(tree[i][j], end= ' ')
    #     print()
    # print()
    print('#{} {}' .format(tc, int(postorder(1))))