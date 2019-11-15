arr = [1, 2, 3, 4]
a = [0]*len(arr)
r= 3
t = [0]*r
def soonyul(n, k):
    if n == k :
        print(arr)

    else:
        for i in range(k,n):
            arr[i], arr[k] = arr[k], arr[i]
            johap(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]


# johap(len(arr),0)

def boboon(n, k):
    if n == k :
        for i in range(n):
            if a[i]:
                print(arr[i], end=" ")
        print()

    else:
        a[k] = 0
        boboon(n, k+1)
        a[k] = 1
        boboon(n, k+1)

# boboon(len(arr), 0)

def johap(n, k, r):
    if k == r:
        print(t)

    elif n == len(arr):
        return

    else:
        t[k] = arr[n]
        johap(n+1, k+1, r)
        johap(n+1, k, r)

johap(0,0, 3)