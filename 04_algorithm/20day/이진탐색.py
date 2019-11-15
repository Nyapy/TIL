import sys

sys.stdin = open('이진탐색.txt')

T = int(input())

def postorder(v):
    global num
    if v != 0:
        postorder(tree[v][0])
        tree[v][3] = num
        num += 1
        postorder(tree[v][1])


for tc in range(1,T+1):
    N = int(input())
    cnt = 1

    tree = [[0]*4 for _ in range(N+1)]

    bi = 1
    num = 1
    while bi <= N and cnt <=N:
        cnt +=1
        if cnt <= N:
            tree[bi][0] = cnt
        cnt +=1
        if cnt <= N:
            tree[bi][1] = cnt
        if cnt <= N+1:
           tree[cnt-1][2] = bi
        if cnt <= N:
            tree[cnt][2] = bi
        bi += 1

    postorder(1)

    print('#{} {} {}' .format(tc, tree[1][3], tree[N//2][3]))