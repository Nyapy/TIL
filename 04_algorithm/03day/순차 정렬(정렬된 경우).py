def sequentialSearch2(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i = i+1

    if i < n and a[i] == key :
        return i

    else:
        return -1

data = [4, 9, 11, 19, 24]
key = 19
print(sequentialSearch2(data, len(data), key))