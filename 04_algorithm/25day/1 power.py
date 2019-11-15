def iter_power(x,n):
    rst = 1
    for i in range(n):
        rst = rst *x

    return rst

def rec_power(x,n):
    if n == 1: return x
    if n % 2 == 0:
    # if n & 1 == 0:
        y = rec_power(x, n//2)
        return y*y
    else:
        y = rec_power(x,(n-1)//2)
        return y*y*x

print(iter_power(2,10))
print(rec_power(2,10))