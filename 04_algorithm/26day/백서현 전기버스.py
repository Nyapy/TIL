def ebus(x, n):
    if c[x] <= n:
        return
    if rslt[0] <= n:
        return
    for i in range(M[x], 0, -1):
        if x + M[x] >= N[0] - 1:
            c[x] = c[x] if c[x] < n else n
            rslt[0] = rslt[0] if rslt[0] < c[x] else c[x]
            return
        c[x] = n
        ebus(x + i, n + 1)
T = int(input())

for testcase in range(1, T + 1):
    N = list(map(int, input().split()))
    M = N[1:] + [0]
    c = [1 << 10] * len(N)
    rslt = [1 << 10]
    ebus(0, 0)
    print("#{} {}".format(testcase, rslt[0]))