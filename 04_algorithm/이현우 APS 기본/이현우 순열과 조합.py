A = [1,2,3,4,5]
N= 3
PA = [0]*N

#1 nPn n개의 원소를 나열하는 경우
def perm(n,k):
    if n == k :
        print(A)

    else:
        for i in range(k, n):
            A[i], A[k] = A[k], A[i]
            perm(n, k+1)
            A[i], A[k] = A[k], A[i]

#2 nPr n개 중 r개를 뽑아 나열하는 경우
def perm2(n,k,q):
    if k == q:
        print(PA)
    else:
        for i in range(k, n):
            A[i], A[k] = A[k], A[i]
            PA[k] = A[k]
            perm2(n, k+1,q)
            A[i], A[k] = A[k], A[i]

#3 nPr n개 중 r개를 뽑아 나열하는 경우(중복 허용)
def perm3(n,k,q):
    if k == q:
        print(Com2)
    else:
        for i in range(n):
            Com2[k] = A[i]
            perm3(n, k+1,q)

Com = [0] * N

#4 nCr n개 중 r개를 뽑는 경우
def comb(n,k):
    if n < k:
        return

    if k == 0 :
        print(Com)

    else:
        Com[k-1] = A[n-1]
        comb(n-1,k-1)
        comb(n-1, k)


Com2= [0]*N


#5 nCr n개 중 r개를 뽑는 경우(중복 허용)
def comb2(n,k):
    if k == 0 :
        print(Com2)
    elif n ==0:
        return
    else:
        Com2[k-1] = A[n-1]
        comb2(n, k-1)
        comb2(n-1, k)


perm(len(A),0)
print("---------------------------------------------------------------------------------------")
perm2(len(A),0, N)
print("---------------------------------------------------------------------------------------")
perm3(len(A), 0,N)
print("---------------------------------------------------------------------------------------")
comb(len(A), N)
print("---------------------------------------------------------------------------------------")
comb2(len(A),N)
