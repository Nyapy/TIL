import sys

sys.stdin = open('공통조상.txt')

T = int(input())

def ancestor(v):
    if v != 0:
        anc.append(v)
        ancestor(tree[v][2])

def answer(a,b):
    for i in a:
        for j in b:
            if i == j :
                ans = i
                return ans

def answer2(v):
    global cnt
    if v != 0:
        cnt +=1
        answer2(tree[v][0])
        answer2(tree[v][1])

for tc in range(1,T+1):
    V, E, A, B = map(int, input().split())
    gansun = list(map(int, input().split()))

    tree = [[0]*3 for _ in range(max(gansun)+1)]

    for i in range(0, len(gansun), 2):
        if tree[gansun[i]][0] == 0:
            tree[gansun[i]][0] = gansun[i+1]
        else :
            tree[gansun[i]][1] = gansun[i+1]
        tree[gansun[i+1]][2] = gansun[i]

    cnt = 0
    anc = []
    ancestor(A)
    a = anc
    anc = []
    ancestor(B)
    b = anc
    dap = answer(a,b)
    answer2(dap)
    print('#{} {} {}' .format(tc, dap, cnt))


