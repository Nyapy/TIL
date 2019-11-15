import sys
sys.stdin = open('b.txt')

arr = list(map(int, input().split()))
k = int(input())
perm_list = []


def perm(n, k):
    if n == k:
        perm_list.append(arr[:])

    else:
        for i in range(k,n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]

perm(len(arr), 0)

perm_list.sort()
ans = ''
for j in perm_list[k-1]:
    ans += str(j)
print(ans)