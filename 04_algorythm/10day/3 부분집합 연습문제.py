N = 10
A = [0 for _ in range(N)]

count = 0
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0

def printSet(n):
    global count
    count += 1
    a = 0
    for i in range(n):
        if A[i]:
            a += data[i]

    if a == 10:
        print("%d : " % (count), end= "" )
        for j in range(n):
            if A[j] :
                print("%d " % data[j], end="")
        print()

def powerSet(n, k, sum):

    if sum > 10 : return

    if n == k:
        if sum == 10:
            printSet(n)

    else :
        if sum <= 10:

            A[k] = 1
            powerSet(n, k+1, sum + data[k])

            A[k] = 0
            powerSet(n, k + 1, sum)

powerSet(N, 0, 0)