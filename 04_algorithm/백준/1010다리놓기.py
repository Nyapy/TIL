import sys

sys.stdin = open("1010다리놓기.txt")

T = int(input())

res = 0

for tc in range(1,T+1):
    N, M = map(int, input().split())
    fac = 1
    zet = 1
    for i in range(M,M-N,-1):
        fac *= i
    for i in range(1, N+1):
        zet *= i

    res = fac//zet

    print(res)