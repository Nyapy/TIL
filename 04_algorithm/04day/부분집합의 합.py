import sys

sys.stdin = open("부분집합의 합_input.txt")

T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, T+1):
    cnt = 0

    N, K = map(int, input().split())


    C = len(A)
    for i in range(1 << C):
        sum = 0
        ss = []
        for j in range(C):
            if i & (1 << j):
                ss += [A[j]]

        # print(ss)

        for k in ss:
            sum += k
        # print(len(ss))
        # print(sum)


        if len(ss) == N and sum == K:
            cnt += 1
    print('#{} {}' .format(tc, cnt))

