n = int(input())
board = [input() for __ in range(n)]
D = '#'
M = '!'
B = '*'
E = '.'

d0, d1 = (
    (r, c)
    for r in range(n)
    for c in range(n)
    if board[r][c] == D
)

visited = [[False] * n for __ in range(n)]

q = [d0]
visited[d0[0]][d0[1]] = True
res = -1

while not visited[d1[0]][d1[1]]:
    res += 1
    nq = []
    for r, c in q:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            while 0 <= nr < n > nc >= 0 and board[nr][nc] != B:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    if board[nr][nc] == M:
                        nq.append((nr, nc))
                nr += dr
                nc += dc
    q = nq

print(res)