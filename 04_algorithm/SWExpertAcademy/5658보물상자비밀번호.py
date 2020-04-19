import sys

sys.stdin = open("5658.txt")

T = int(input())

#
# print(ord("F"))

for tc in range(1,T+1):
    N,K = map(int, input().split())

    num = N//4

    numbers = list(input())
    for n in range(N):
        if 48 <= ord(numbers[n]) <= 58:
            numbers[n] = ord(numbers[n])-48
        elif 65 <= ord(numbers[n]) <= 70:
            numbers[n] = ord(numbers[n]) - 55
    # print(numbers)

    candi = set()

    for i in range(num):
        for j in range(N-1,-1,-num):
            tem_value = 0
            for k in range(num):
                index = (i + j - k)%N
                tem =  numbers[index]
                tem_value += tem*(16**k)
            candi.add(tem_value)

    a = list(candi)
    a.sort()
    a.reverse()
    print("#{} {}" .format(tc, a[K-1]))

