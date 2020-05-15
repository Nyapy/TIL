import sys

sys.stdin = open("2112.txt")

from copy import deepcopy
from itertools import combinations
T = int(input())

def ISIT(copy):

    for j in range(W):
        cnt = 1
        tem = copy[0][j]
        for i in range(1,D):
            if tem == copy[i][j]:
                cnt += 1
                tem = copy[i][j]
                if cnt == K:
                    break
            else:
                tem = copy[i][j]
                cnt = 1
        if cnt < K:
            return False

    return True


def comb(s,n,k):
    global flag, ans
    if flag:
        return
    if D-n < s-k:
        return
    if k == s :
        A = [0] * D
        for j in range(s+1):
            AB(j,0,0,A)
            if flag:
                ans = s
                break

        return

    else:
        comb(s,n+1,k)
        select[n] = 1
        comb(s,n+1, k+1)
        select[n] = 0


def AB(s,n,k,A):
    global flag, ans
    if flag:
        return
    if D-n < s-k:
        return
    if k == s :
        copy_film = deepcopy(film)
        for a in range(D):
            if select[a] == 1:
                if A[a] == 1:
                    copy_film[a] = [0] * W
                else :
                    copy_film[a] = [1] *W

        flag = ISIT(copy_film)

        return

    else:
        if select[n] == 1:
            AB(s,n+1,k,A)
            A[n] = 1
            AB(s,n+1, k+1,A)
            A[n] = 0
        else:
            AB(s,n+1,k,A)


for tc in range(1):
    D,W,K = map(int, input().split())

    film = [list(map(int, input().split())) for _ in range(D)]
    ans = 0
    select = range(D)
    flag = False
    if K == 1:
        ans = 0
    else:
        # for i in range(1+D):
        #     comb(i,0,0)
        #     if flag:
        #         break
        for i in range(1+D):
            if flag:
                break
            a=combinations(select, i)

            for j in a:
    print("#{} {}" .format(tc, ans))
