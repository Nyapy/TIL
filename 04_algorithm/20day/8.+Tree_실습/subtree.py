def preorder(node):
    global cnt
    if node != 0:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

import sys
sys.stdin = open("subtree_input.txt", "r")
T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    tree = [[0 for _ in range(3)] for _ in range(E+2)]  #left, right, parent
    temp = list(map(int, input().split()))
    cnt = 0
    for i in range(E):
        n1 = temp[i * 2]
        n2 = temp[i * 2 + 1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1
    preorder(N)
    print(f"#{tc+1} {cnt}")