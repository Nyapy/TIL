def makeT(n):
    global idx, N
    if n <= N:
        makeT(n*2)          #왼쪽 서브트리 방문
        tree[n] = idx       #중위순회로 현재 노드값 저장
        idx += 1
        makeT(n*2+1)        #오른쪽 서브트리 방문

import sys
sys.stdin = open("이진탐색_input.txt")
T = int(input())

for tc in range(T):
    N = int(input())

    idx = 1
    tree = [0 for _ in range(N+1)]  #리스트를 이용한 완전 이진 트리 저장
    makeT(1)
    print('#{} {} {}'.format(tc+1, tree[1], tree[N // 2]))