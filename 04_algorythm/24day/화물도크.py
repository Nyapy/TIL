import sys
sys.stdin = open('화물도크.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    se  = [list(map(int, input().split())) for _ in range(N)]


    se.sort(key=lambda x:x[1])

    max_cnt = 0
    for i in range(N):
        t = se[i]
        k = i+1
        cnt = 1
        while k < N:
            if se[k][0] >= t[1] :
                t = se[k]
                cnt += 1
                k+=1

            else:
                k+=1
        if max_cnt < cnt :
            max_cnt = cnt

    print('#{} {}' .format(tc, max_cnt))