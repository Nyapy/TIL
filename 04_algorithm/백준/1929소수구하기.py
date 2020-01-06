import sys

sys.stdin = open("1929소수구하기.txt")

M, N = map(int, input().split())

prime = []

for n in range(2, N+1):
    if n == 2:
        prime.append(n)

    else:
        flag = 0
        for a in prime:
            if a**2 > n:
                break
            if n % a == 0:
                flag = 1
                break

        if flag == 0:
            prime.append(n)

for k in prime:
    if k >= M:
        print(k)