def perm(d, g, arr):
    if d == g:
        print(arr)
        return
    for i in range(len(lst)):
        if not c[i]:
            c[i] = 1
            perm(d + 1, g, arr + [lst[i]])
            c[i] = 0

arr =[]
lst = [1,2,3,4,5]
c = [0]*len(lst)

perm(0, 3, arr)