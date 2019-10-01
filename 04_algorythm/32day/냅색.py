def powerset(n,k,curw, curv):
    global ans
    if curw > W:
        return

    if n == k:
        if curv > ans:
            ans = curv

    else:
        if curw <= W:
            A[k] = 1
            powerset(n, k+1, curw+weight[k], curv+value[k])
            A[k] = 0
            powerset(n, k+1, curw, curv)

W = 10
n = 4

weight = [5, 4, 6, 3]
value = [10,40,30,50]
A = [0] * n
ans = 0

powerset(n,0,0,0)

print("{}" .format(ans))