import sys

sys.stdin = open('농작물 수확하기.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    # print(farm)
    cnt = 0
    tot = 0
    N2 = N//2
    for i in range(N):
        if i <= N//2:
            for j in range((N//2)-cnt, (N//2)+cnt+1):
                tot += farm[i][j]
                cnt +=1
        if i > N//2:
            for j in range((N//2)-cnt, (N//2)+cnt+1):
                tot += farm[i][j]
                cnt -=1

    # print(farm)
    # print(N)
    # print(farm[0][2])

    print(tot)