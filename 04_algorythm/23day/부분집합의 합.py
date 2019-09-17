data = [1,2,3,4,5,6,7,8,9,10]
A= [0]*len(data)



def powerset(n,k,s):
    if k == n :
        if s == 10:
            for i in range(n):
                if A[i]:
                    print("{}" .format(data[i]), end = " ")
            print()

    else:
        if s <= 10:
            A[k] = 1
            powerset(n,k+1,s+data[k])
            A[k] = 0
            powerset(n, k+1, s)

powerset(10, 0, 0)