def myprint(q):
    print(T)
def comb(n, r, q, cnt):
    if cnt == q:
        myprint(q)
    else:
        if n-r >= q-cnt:
            for i in range(r, n):
                T[cnt] = A[i]
                comb(n,i+1,q, cnt+1)

q= 3

A = [1, 2, 3, 4, 5]
T = [0] * q

comb(5, 0, q, 0)
