T = int(input())



for tc in range(1, T+1):
    A, B = map(int, input().split())
    N = A // B
    s= 0
    for i in range(1, N+1):
        s += i*2-1
    print("#{} {}".format(tc, s))