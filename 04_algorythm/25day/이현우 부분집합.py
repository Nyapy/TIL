N= 3
A= []
data = [1,2,3]

def printSet(n):
    print(A)

def powerset(n,k):
    if n ==k:
        printSet(n)

    else:

        A[k] = 0
        powerset(n, k+1)
        A[k] = data[k]
        powerset(n, k+1)

powerset(N, 0)