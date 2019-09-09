import sys

sys.stdin = open('중위순회.txt')

T = 10

def inorder(v):
    if v != 0:
        inorder(tree[v][1])
        print('{}' .format(tree[v][0]), end = '')
        inorder(tree[v][2])

for tc in range(1,1+T):
    N = int(input())

    sun = [list(input().split()) for _ in range(N)]

    tree = [[0]*4 for _ in range(N+1)]

    # print(sun)

    for i in range(len(sun)):
        for j in range(len(sun[i])):
            if len(sun[i]) == 4:
                tree[int(sun[i][0])][0]= sun[i][1]
                tree[int(sun[i][0])][1] = int(sun[i][2])
                tree[int(sun[i][0])][2] = int(sun[i][3])

                tree[int(sun[i][2])][3] = int(sun[i][0])
                tree[int(sun[i][3])][3] = int(sun[i][0])

            elif len(sun[i]) == 3:
                tree[int(sun[i][0])][0] = sun[i][1]
                tree[int(sun[i][0])][1] = int(sun[i][2])

                tree[int(sun[i][2])][3] = int(sun[i][0])


            elif len(sun[i]) == 2:
                tree[int(sun[i][0])][0] = sun[i][1]

    # print(tree)
    print('#{}' .format(tc), end = ' ')

    inorder(1)
    print()