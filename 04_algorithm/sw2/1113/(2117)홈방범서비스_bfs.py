def f(x, y):  # bfs
    deq = collections.deque()
    deq.append((x, y))   # EnQueue
    visited = [[0] * N for _ in range(N)]  # N * N 초기화
    visited[x][y] = 1
    k_home = [0] * (N + 2)  # 거리별 집 수

    while (len(deq) != 0):
        x, y = deq.popleft()

        if city[x][y] == 1:
            k_home[visited[x][y]] += 1  # 거리별 집 수
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[x][y] <= N and visited[nx][ny] == 0:  #  N+1까지
                visited[nx][ny] = visited[x][y] + 1
                deq.append((nx, ny))

    # 서비스 거리 이내의 집 수 누적 및 비용과 비교
    cnt = 0
    for i in range(1, N + 2):
        k_home[i] += k_home[i - 1]  # 범위 q 이내의 집 누적
        if cost[i] <= k_home[i] * M:
            cnt = k_home[i]
    return cnt

import collections
import sys
sys.stdin = open("(2117)홈방범서비스_input.txt")
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())
cost = [0] * 22
for k in range(1, 22):  # 영역의 크기별 비용
    cost[k] = k * k + (k - 1) * (k - 1)

for tc in range(1, T + 1):
    # 도시의 크기 N과 하나의 집이 지불할 수 있는 비용 M
    N, M = map(int, input().split())  # 5 ≤ N ≤ 20, 1 ≤ M ≤ 10
    city = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(N):
        for j in range(N):
            ret = f(i, j)
            if maxV < ret:
                maxV = ret
    print('#{} {}'.format(tc, maxV))