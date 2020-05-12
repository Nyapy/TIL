import sys

sys.stdin = open('5653.txt')

T = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for tc in range(1,1+T):
    N,M,K = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(N)]

    # print(grid)
    # 비/활/죽, 생명력, 비/활동시간
    #
    active = [[[-1,-1,-1] for _ in range(M+K)] for _ in range(N+K)]
    for i in range(N):
        for j in range(M):
            if grid[i][j]:
                active[i+(K//2)][j+(K//2)] = [0,grid[i][j],0]
    time = 0
    while time < K:
        tem = [[0 for _ in range(M + K)] for _ in range(N + K)]
        for i in range(N+K):
            for j in range(M+K):
                if active[i][j][1] :
                    t = active[i][j]
                    if t[0] == 0: #비활성 상태일때
                        t[2] += 1
                        if t[2] == t[1]:
                            t[0] = 1
                            t[2] = 0
                        active[i][j] = t
                    elif t[0] == 1: #활성 상태일때
                        for k in range(4):
                            nx = j + dx[k]
                            ny = i + dy[k]
                            if 0<= nx < M+K and 0 <= ny <N+K and active[ny][nx] == [-1,-1,-1]:
                                if tem[ny][nx] == 0 or (tem[ny][nx][1] < t[1] and tem[ny][nx][0] == 0 and tem[ny][nx][2] == 0):
                                    tem[ny][nx] = [0,t[1],0]
                        t[2] += 1
                        if t[2] == t[1]:
                            t[0] = -1
                        active[i][j] = t
        for i in range(N + K):
            for j in range(M + K):
                if tem[i][j]:
                    active[i][j] = tem[i][j]
        time += 1

    ans = 0
    for i in range(N+K):
        for j in range(M+K):
            if active[i][j][0] >= 0:
                ans += 1

    print("#{} {}" .format(tc, ans))