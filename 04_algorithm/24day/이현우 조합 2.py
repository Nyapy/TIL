def myprint(q):
    print(T)


def comb(n, r, q):
    if r == q:
        myprint(q)
    elif n == len(A):
        return
    else:
        T[r] = A[n]
        comb(n+1, r+1, q)
        comb(n+1, r, q)

A = [1, 2, 3, 4, 5]
T = [0] * 3

comb(0, 0, 3)