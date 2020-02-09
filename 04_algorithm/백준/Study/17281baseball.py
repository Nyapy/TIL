import sys

sys.stdin = open("17281.txt")

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

seq = list(range(1,10))
seq[0],seq[3] = seq[3],seq[0]
print(seq)

a = 0
now = 0
base = [0,0,0,0]
out = 0


sit = [0,1,2,3,4]

def perm(k, n, re):
    global now, out
    if k < 9:
        if k == 3:
            perm(k+1,n)
        else:
            for i in range(k,n):
                arr[k], arr[i] = arr[i], arr[k]
                perm(k+1,n)
                arr[k], arr[i] = arr[i], arr[k]

    else:
        a = k %9
        arr[now][[seq[k]]]