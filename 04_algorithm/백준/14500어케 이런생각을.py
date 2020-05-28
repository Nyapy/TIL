import sys
input = sys.stdin.readline

def f(arr,n,m):
    res=0
    for i in range(1,n+1):
        for j in range(1, m):
            subs=[arr[i-1][j],arr[i-1][j+1],arr[i][j-1],arr[i][j+2],arr[i+1][j],arr[i+1][j+1]]
            subs.sort(reverse=True)
            tmp = arr[i][j]+arr[i][j+1]+subs[0]+subs[1]
            if tmp > res:
                res=tmp
    for i in range(1,n):
        for j in range(1, m+1):
            subs=[arr[i-1][j],arr[i][j-1],arr[i][j+1],arr[i+1][j-1],arr[i+1][j+1],arr[i+2][j]]
            subs.sort(reverse=True)
            tmp = arr[i][j]+arr[i+1][j]+subs[0]+subs[1]
            if tmp > res:
                res=tmp
    return res

def BOJ_14500():
    n,m = map(int,input().split())
    p = [[0]*(m+2) for _ in range(n+2)]
    for i in range(1,n+1):
        s = list(map(int,input().split()))
        for j in range(1,m+1):
            p[i][j]=s[j-1]
    print(f(p,n,m))
BOJ_14500()