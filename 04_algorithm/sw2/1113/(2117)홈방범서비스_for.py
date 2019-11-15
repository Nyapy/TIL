def solve():
    global ans
    # (x,y)좌표를 기준으로 k= N + 1 -> 1 로 감소시킴
    for x in range(N):
        for y in range(N):
            for k in range(N + 1, 0, -1):  # N+1부터 시작해야 모두 커버 가능
                cnt = 0
                for hx, hy in Home:
                    if abs(x - hx) + abs(y - hy) < k: # (x,y) 좌표에서 집까지 거리 < k
                        cnt += 1
                if cnt < ans: break
                if M * cnt - cost[k] >= 0 and ans < cnt:
                    ans = cnt
                    break

import sys
sys.stdin = open("(2117)홈방범서비스_input.txt")

# 비용을 미리 계산
cost = [0] * 22
cost[1] = 1
for i in range(2, 22):
    cost[i] = cost[i - 1] + 4 * (i - 1)

T = int(input())
for tc in range(1, T + 1):
    ans = 0
    # 도시의 크기 N과 하나의 집이 지불할 수 있는 비용 M
    N, M = map(int, input().split())
    Home = []  # 집 좌표를 저장
    for i in range(N):
        MAP = list(map(int, input().split()))
        for j in range(N):
            if MAP[j]: Home.append((i, j))

    solve()

    print('#{} {}'.format(tc, ans))