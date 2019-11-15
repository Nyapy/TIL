import sys
sys.stdin = open('컨테이너운반.txt')

T = int(input())

for tc in range(1,1+T):
    N,M = map(int, input().split())
    weight = list(map(int, input().split()))
    volume = list(map(int, input().split()))

    weight.sort(reverse=1)
    volume.sort(reverse=1)

    print(weight)
    print(volume)
    total = 0

    while len(weight) > 0 and len(volume) > 0:
        a= volume.pop(0)

        for i in range(len(weight)):
            if a >= weight[i] :
                total += weight.pop(i)
                break
    print('#{} {}' . format(tc, total))