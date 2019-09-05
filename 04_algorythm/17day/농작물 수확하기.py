import sys

sys.stdin = open('농작물 수확하기.txt')

T = int(input())

for tc in range(1,1+T):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    tot = 0
    # print(farm)
    cnt = 1

    for i in range(N):
        if i <= N//2:
            for j in range(N//2-i,N//2+1+i):
                tot += farm[i][j]
        if i > N//2:
            for j in range(cnt,N-cnt):
                tot += farm[i][j]
            cnt +=1

    print('#{} {}' .format(tc, tot))