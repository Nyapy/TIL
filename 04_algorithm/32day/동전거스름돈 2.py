
N = 20

change= [0,1,5, 10, 16]

want = [[0]*(N+1) for _ in range(len(change))]

for i in range(N+1):
    want[0][i] = N+1

for i in range(1, len(change)):
    for j in range(1, N+1):
        if j < change[i]:
            want[i][j] = want[i-1][j]

        else:
            want[i][j] = min(want[i][j-change[i]]+1, want[i-1][j])


for i in range(len(change)):
    for j in range(1, N+1):
        print("{} " .format(want[i][j]), end = "")

    print()