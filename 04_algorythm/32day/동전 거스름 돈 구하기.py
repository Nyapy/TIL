import sys

sys.stdin = open("거스름돈.txt")

N = int(input())

C = int(input())

c1, c2, c3, c4, c5 = map(int, input().split())

m = 10000

def change(n,s,k):
    global m

    if k > m:
        return

    if n == s:
        a= k
        if a < s :
            m = a
        return

    else:
        if s+c5 <= n:
            change(n, s+c5, k + 1)
        if s+c4 <= n:
            change(n, s+c4, k + 1)
        if s + c1 <= n:
            change(n, s+c1, k+1)
        if s+c2 <= n:
            change(n, s+c2, k + 1)
        if s+c3 <= n:
            change(n, s+c3, k + 1)





change(N,0,0)

print(m)