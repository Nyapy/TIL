import sys

sys.stdin = open('전자카트.txt')

T = int(input())

def perm(n,k,s):
    global min_cun
    if n == k:
        s += field[seq[k-1]][0]
        if min_cun > s:
            min_cun = s

    else:
        if s < min_cun:
            for i in range(k,n):
                seq[k],seq[i] = seq[i], seq[k]
                if k == 0:
                    perm(n, k+1, s+field[0][seq[k]])
                else:
                    perm(n, k+1, s+field[seq[k-1]][seq[k]])
                seq[k], seq[i] = seq[i], seq[k]


for tc in range(1,1+T):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    min_cun = 100*N

    seq = [i for i in range(1,N)]

    perm(len(seq), 0, 0)

    print('#{} {}' .format(tc, min_cun))