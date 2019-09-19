A = [11, 45, 23, 81, 28, 34]
r = len(A)-1
l = 0

def Hoare(A, l, r):
    p = A[l]
    i = l
    j = r
    while i <= j:
        while A[i] <= p and i < r :
            i += 1

        while A[j] >= p and j > l:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]

    return j

def HP(a, l, r):
    if l == r:
        return
    elif l < r:
        p = Hoare(a, l, r)
        HP(A,l, p -1)
        HP(A, p+1, r)

HP(A,l, r)

print(A)