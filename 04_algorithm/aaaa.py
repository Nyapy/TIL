N = 3
T = list(range(N+1))
print(T)
for i in range(1,1<<N):
    for j in range(N):
        if i & (1<<j):
            print(T[j], end=" ")
    print()

