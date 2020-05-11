arr = [2, 2, 2, 2, 3, 3, 5, 6]

N = len(arr)

def comb(n,k,q):
    if N-k < n-q:
        return
    if n == q:
        print(com)
        return

    else:
        com[k] = 1
        comb(n, k+1, q+1)
        com[k] = 0
        comb3q(n, k+1, q)

com = [0] * N

for i in range(2, N+1):
    comb(i,0, 0)