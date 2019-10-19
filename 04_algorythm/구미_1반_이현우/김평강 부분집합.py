for i in range(1, 1<<4):
    arr = []
    for j in range(4):
        if i&1<<j:
            arr.append(j)
    print(arr)