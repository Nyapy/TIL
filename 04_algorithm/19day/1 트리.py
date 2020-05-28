import sys

sys.stdin = open('1 트리.txt')

a = list(map(int, input().split()))

Tree = [[0]*3 for _ in range(max(a)+1)]

def preorder(v):

    print(v)
    if Tree[v - 1][0] != 0:
        preorder(Tree[v-1][0])
    if Tree[v - 1][1] != 0:
        preorder(Tree[v-1][1])


for i in range(0,len(a), 2):
    if Tree[a[i]-1][0] == 0:
        Tree[a[i]-1][0] = a[i+1]
    elif Tree[a[i]-1][0] != 0:
        Tree[a[i]-1][1] = a[i+1]

    Tree[a[i+1]-1][2] = a[i]

# for i in range(len(Tree)):
#     for j in range(3):
#
#         print(Tree[i][j], end = ' ')
#     print()
#
preorder(1)