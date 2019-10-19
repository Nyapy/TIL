arr =[]
lst = [1,2,3,4,5]
c = [0]*len(lst)

def perm(d, g, arr):
    if d == g:
        print(arr)
        return
    for i in range(len(lst)):
        if not c[i]:
            c[i] = 1
            perm(d + 1, g, arr + [lst[i]])
            c[i] = 0


def dperm(d, g, arr):
    if d == g:
        print(arr)
        return
    for i in range(len(lst)):
        dperm(d + 1, g, arr + [lst[i]])


def comb(idx, d, g, arr):
    if d == g:
        print(arr)
        return
    for i in range(idx, len(lst)):
        comb(i + 1, d + 1, g, arr + [lst[i]])

# perm(0, 3, [])
comb(0, 0, 3, [])

perm(0, 3, arr)