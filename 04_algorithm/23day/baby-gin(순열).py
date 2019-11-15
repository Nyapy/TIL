arr = [6,6,7,7,6,7]


def babygin():
    check = 0
    global flag
    if arr[0] == arr[1] and arr[1] == arr[2]:check += 1
    if arr[3] == arr[4] and arr[4] == arr[5]:check += 1

    if arr[0]+1 == arr[1] and arr[1]+1 == arr[2]: check +=1
    if arr[3]+1 == arr[4] and arr[4]+1 == arr[5]: check +=1
    if check ==2:
        flag = 1
        return
def perm(n,k):

    if n == k:
        babygin()
        if flag == 1:
            return

    for i in range(k,n):
        arr[i], arr[k] = arr[k], arr[i]
        perm(n, k+1)
        arr[i], arr[k] = arr[k], arr[i]