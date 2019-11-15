import sys

sys.stdin = open('homesecurity.txt')

T = int(input())

def security(x,y,K):
    global maxnum
    cnt = 0

    for i in range(y-(K-1), y+(K-1)+1):
        if 0 <= i < N :
            xk = abs(i - y)
            for j in range(x-(K-1)+xk, x+(K-1)+1-xk):
                if j >= 0 and j < N:
                    if G[i][j] == 1:
                        cnt += 1

    if cnt*M < K*K+(K-1)*(K-1):
        return
    else:
        if cnt > maxnum:
            maxnum = cnt

for tc in range(1,T+1):
    N, M = map(int, input().split())

    G = [list(map(int,input().split())) for _ in range(N)]
    maxnum = 1

    house = 0
    for i in range(N):
        for j in range(N):
            if G[i][j] == 1:
                house +=1

    mv = M*house

    k = 1
    while k*k+(k-1)*(k-1) <= mv:
        K= k
        k += 1

    while K > 0 :
        for i in range(N):
            for j in range(N):
                security(i, j, K)
        K -=1
        if K > 1:
            if maxnum >1:
                break

    print('#{} {}' .format(tc, maxnum))