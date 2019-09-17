def hap(k):
    if k == 1:
        return 1
    else:
        return k+hap(k-1)

print(hap(10))