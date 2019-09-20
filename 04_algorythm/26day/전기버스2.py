import sys

sys.stdin = open('전기버스2.txt')

T = int(input())

for tc in range(1,1+T):
    bus_stop = list(map(int, input().split()))
    N = bus_stop[0]
    max_b = bus_stop[1]
    i = 1
    cnt  = 0


    while i < N:
        if i+max_b < N:
            for j in range(i+1, i+max_b+1):
                bet = bus_stop[j]
                if j+bet >= i+max_b:
                    max_b = bet
                    i = j
            cnt += 1
        elif i+max_b >= N:
            break

    print("#{} {}" .format(tc, cnt))