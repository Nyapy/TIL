def myprint(q):
    print(t)

def perm(n, r, q):
    if r == q:
        myprint(q)

    else:
        for i in range(r,n):
            a[i], a[r] = a[r], a[i]
            t[r] = a[r]
            perm(n,r+1,q)
            a[i], a[r] = a[r], a[i]
a = [1,2,3,4]
t = [0]*3

perm(4,0,3)