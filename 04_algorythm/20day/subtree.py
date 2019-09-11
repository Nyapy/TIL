import sys

sys.stdin = open('subtree.txt')

T = int(input())

def preorder(v):
    global  cnt
    if v != 0:
        cnt += 1
        preorder(tree[v][0])
        preorder(tree[v][1])
for tc in range(1,T+1):
    E,N = map(int, input().split())
    tem = list(map(int, input().split()))
    tree = [[0]*3 for _ in range(max(tem)+1)]
    cnt = 0
    for i in range(0,2*E, 2):
        if tree[tem[i]][0] == 0:
            tree[tem[i]][0] = tem[i+1]
        else:
            tree[tem[i]][1] = tem[i+1]
        tree[tem[i+1]][2] = tem[i]
    preorder(N)
    print('#{} {}' .format(tc, cnt))