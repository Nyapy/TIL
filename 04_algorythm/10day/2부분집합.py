count = 0

N = 3

A = [0 for _ in range(N)] # 원소의 포함여부 저장(0,1)
data = [1, 2, 3]

def printSet(n):
    global count
    count +=1
    print("%d : " % (count), end= "" )
    for i in range(n):
        if A[i] :
            print("%d " % data[i], end="")
    print()


def powerset(n, k):
    if n == k:
        printSet(n)
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)


powerset(N, 0)