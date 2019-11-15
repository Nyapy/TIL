'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
-> 27
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
-> 9
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
-> 3
'''

# 연구소

import collections
def BFS(x, y):
    deq = collections.deque()

    copied[x][y] = 2
    deq.append((x, y))
    while deq:
        x, y = deq.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            tx, ty = x + dx, y + dy
            if tx < 0 or tx >= N or ty < 0 or ty >= M or copied[tx][ty]:
                continue
            copied[tx][ty] = 2
            deq.append((tx, ty))

#-----------------------------------------------------------

N, M = map(int, input().split())
arr, wall, virus = [], [], []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j] == 0:   # 빈칸
            wall.append((i, j))
        if arr[i][j] == 2:
            virus.append((i, j))

copied = [[0] * M for _ in range(N)]
ans = 0
NW = len(wall)

# 무조건 3개
for i in range(NW):
    for j in range(i + 1, NW):
        for k in range(j + 1, NW):
            # -----------------------------------
            # 복사
            for r in range(N):
                for c in range(M):
                    copied[r][c] = arr[r][c]
            # -----------------------------------
            copied[wall[i][0]][wall[i][1]] = 3
            copied[wall[j][0]][wall[j][1]] = 3
            copied[wall[k][0]][wall[k][1]] = 3

            for x, y in virus:
                BFS(x, y)

            cnt = 0
            for lst in copied:
                cnt += lst.count(0)

            ans = max(ans, cnt)

print(ans)