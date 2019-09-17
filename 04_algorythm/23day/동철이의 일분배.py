import sys

sys.stdin = open('동철이의 일분배.txt')

T = int(input())

# def potential(pot):


def perm(n, k, pot):
    global max_pot

    if n == k :
        if max_pot < pot:
            max_pot = pot

    else:
        if pot > max_pot:
            for i in range(k,n):
                work[k], work[i] = work[i], work[k]
                perm(n, k+1, pot*poten[k][work[k]]/100)
                work[k], work[i] = work[i], work[k]


for tc in range(1,1+T):
    N = int(input())
    poten = [list(map(int, input().split())) for _ in range(N)]
    work = [0]*N
    max_pot = 0

    for i in range(N):
        work[i] = i

    perm(N, 0, 1)

    print('#{} {:.6f}' .format(tc, max_pot*100))