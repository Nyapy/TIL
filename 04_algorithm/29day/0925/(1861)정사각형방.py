import collections
import sys
sys.stdin = open("(1861)정사각형방_input.txt")

def bfs(x, y):
    max = 0
    deq = collections.deque()
    deq.append((x, y))
    visit[x][y] = 1
    while deq:
        x, y = deq.popleft()
        if visit[x][y] > max: max = visit[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:continue
            if data[x][y] + 1  == data[nx][ny]:
                deq.append((nx,ny))
                visit[nx][ny] = visit[x][y] + 1
    return max

def dfs(x, y):
    max = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx == N or ny == N: continue
        if data[x][y] + 1 == data[nx][ny]:
            ret = dfs(nx, ny)
            if ret > max: max = ret
    return max + 1

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]   # 실제 거리만 체크함.
    ans = 987654321
    max = 0

    for x in range(N):
        for y in range(N):
            #ret = dfs(x, y)
            ret = bfs(x, y)
            if ret > max:
                max = ret
                ans = data[x][y]
            elif ret == max and ans > data[x][y] : #같으면 작은 걸로
                ans = data[x][y]

    print("#{} {} {}".format(tc, ans, max))
