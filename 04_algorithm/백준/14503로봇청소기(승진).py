import sys

sys.stdin = open('14503.txt')

def Cleaning(r, c, d):
    global rst
    global ans
    if d == 0:  # 북쪽을 바라볼때
        dy = [-1, 0, 1, 0]  # 서남동북
        dx = [0, 1, 0, -1]
    elif d == 1:  # 동쪽을 바라볼때
        dy = [0, -1, 0, 1]  # 북서남동
        dx = [-1, 0, 1, 0, ]
    elif d == 2:  # 남쪽을 바라볼때
        dy = [1, 0, -1, 0]  # 동북서남
        dx = [0, -1, 0, 1]
    elif d == 3:  # 서쪽을 바라볼때
        dy = [0, 1, 0, -1]  # 남동북서
        dx = [1, 0, -1, 0]
    if MAP[r][c] == 1: return
    if visited[r][c] == 0 and MAP[r][c] == 0:
        visited[r][c] = rst
        rst += 1
        ans += 1
    cnt = 0
    for idx in range(4):
        x = r + dx[idx]
        y = c + dy[idx]
        # if x < 0 or x >= N or y < 0 or y >= M: continue
        if 0 <= x < N and 0 <= y < M and MAP[x][y] == 0 and visited[x][y] == 0:
            if dy[idx] == -1 and dx[idx] == 0: d = 3
            elif dy[idx] == 0 and dx[idx] == 1: d = 2
            elif dy[idx] == 1 and dx[idx] == 0: d = 1
            else: d = 0
            Cleaning(x, y, d)
        else:
            cnt += 1
            continue
    if cnt >= 3:
        a = r + dx[1]
        b = c + dy[1]
        if MAP[a][b] == 0:
            Cleaning(a, b, d)
        else: return
N, M = map(int, input().split())
r, c, d = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
ans = 0
rst = 1
Cleaning(r, c, d)
print(ans)
print(rst)