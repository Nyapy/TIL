import sys

sys.stdin = open('1 트리.txt')

N = int(input())
a = list(map(int, input().split()))

Tree = [[0]*3 for _ in range(max(a)+1)]

def preorder(v):
    if v != 0:
        print("{}" .format(v), end = ' ')
        preorder(Tree[v][0])
        preorder(Tree[v][1])
def inorder(v):
    if v != 0:
        preorder(Tree[v][0])
        print("{}" .format(v), end = ' ')
        preorder(Tree[v][1])
def postorder(v):
    if v != 0:
        preorder(Tree[v][0])
        preorder(Tree[v][1])
        print("{}" .format(v), end = ' ')

for i in range(0,len(a), 2):
    if Tree[a[i]][0] == 0:
        Tree[a[i]][0] = a[i+1]
    elif Tree[a[i]][0] != 0:
        Tree[a[i]][1] = a[i+1]

    Tree[a[i+1]][2] = a[i]

for i in range(len(Tree)):
    for j in range(3):
        print(Tree[i][j], end = ' ')
    print()

preorder(1)
print()
inorder(1)
print()
postorder(1)