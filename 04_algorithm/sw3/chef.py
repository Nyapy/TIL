import sys

sys.stdin = open('chef.txt')

T = int(input())

def comb(n,k,q):
    global Total, mindif
    if k == q:
        A = []
        B = []
        for i in range(len(ing)):
            if ing[i]:
                A.append(i+1)
            else:
                B.append(i+1)
        # print(A,B)

        Total = 0
        cooking(A, 0, 0)
        AS = Total

        Total = 0
        cooking(B, 0, 0)
        BS = Total

        dif = abs(AS-BS)

        if dif < mindif:
            mindif = dif


    elif N - n < q-k:
        return

    else:
        ing[n] = 1
        comb(n+1, k+1, q)
        ing[n] = 0
        comb(n+1, k, q)


def cooking(G,n,k):
    global Total
    if k == 2:
        Total += synergy[selected[0]][selected[1]]+synergy[selected[1]][selected[0]]
    elif len(G)-n < 2-k:
        return
    else:
        selected[k] = G[n]
        cooking(G, n+1, k+1)
        selected[k] = 0
        cooking(G, n+1, k)


for tc in range(1, T+1):
    N = int(input())

    synergy = [0]+[[0]+list(map(int,input().split())) for _ in range(N)]

    mindif = 20000
    selected = [0,0]
    half = N//2
    ing =[0]*N

    comb(0, 0, half)

    print("#{} {}" .format(tc, mindif))
