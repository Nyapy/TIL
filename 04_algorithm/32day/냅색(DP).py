
W = 10
n = 4

weight = [0, 5, 4, 6, 3]
value = [0, 10,40,30,50]
ans = 0

K = [[0 for _ in range(50)] for __ in range(50) ]

for i in range(1, n+1):
    for j in range(1,W+1):
        if j < weight[i]:
            K[i][j] = K[i-1][j]
        else:
            K[i][j] = max(K[i-1][j-weight[i]]+value[i], K[i-1][j])

for i in range(1,n+1):
    for j in range(1, W+1):
        print("{} " .format(K[i][j]), end = "")

    print()