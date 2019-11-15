import sys

sys.stdin = open('정곤이의 단조 증가하는 수.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    l = []

    max = -1
    flag = 0
    data.sort(reverse=True)
    for i in range(N - 1):
        for j in range(i + 1, N - 1):
            a = data[i] * data[j]
            if max > a:
                continue
            end = []
            while a:
                end.append(a % 10)
                a //= 10
            for k in range(len(end) - 1):
                if end[k] < end[k + 1]:
                    break
                if k == len(end) - 2:
                    max = data[i] * data[j]
    print("#{} {}".format(tc, max))
