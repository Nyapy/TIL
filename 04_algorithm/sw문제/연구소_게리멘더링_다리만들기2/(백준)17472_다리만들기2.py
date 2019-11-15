#-------------------------
# 다리만들기
#--------------------------
'''
7 8
0 0 0 0 0 0 1 1
1 1 0 0 0 0 1 1
1 1 0 0 0 0 0 0
1 1 0 0 0 1 1 0
0 0 0 0 0 1 1 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
-> 9
'''
import sys
import collections

#find_set
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

#각 섬간의 다리(간선)의 길이 구하기
def calc_edge():
    for i in range(1, no + 1):
        for x, y in islands[i]:
            for mode in range(4):
                nx, ny = x + dx[mode], y + dy[mode]
                cnt = 0
                while 0 <= nx < N and 0 <= ny < M:
                    if MAP[nx][ny] == i: break  # 같은 섬 내부이면
                    if MAP[nx][ny]:             # 다른 섬에 도착하면
                        if 1 < cnt < G[i][MAP[nx][ny]]:  # 거리가 1보다 크고 인접행렬 값보다 작아야
                            G[i][MAP[nx][ny]] = G[MAP[nx][ny]][i] = cnt
                        break
                    cnt += 1
                    nx, ny = nx + dx[mode], ny + dy[mode]  # 한방향으로 계속 전진

# 섬들의 좌표 찾기
def DFS(x, y, pos, no):
    visit[x][y] = 1
    MAP[x][y] = no  # 섬의 번호로 변경
    pos.append((x, y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] and not visit[nx][ny]:
            DFS(nx, ny, pos, no)
# ----------------------------------------------------
# 1 ≤ N,  M ≤ 10
# 3 ≤ N × M ≤ 100
# 2 ≤ 섬의 개수 ≤ 6
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())    # 지도 세로, 가로 크기
MAP = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
islands = [[]]  # 각 섬의 좌표값들을 저장(0번 skip)
no = 0  # 섬의 수
for i in range(N):
    for j in range(M):
        if MAP[i][j] and not visit[i][j]:
            no += 1
            pos = []
            DFS(i, j, pos, no)
            islands.append(pos)

# 각 섬간의 다리의 길이 구하기
G = [[100] * (no + 1) for _ in range(no + 1)]  #인접행렬(가중치 무한대로 초기화)
calc_edge()

# 간선의 배열 (좌표와 간선의 길이)
Edge = []
for i in range(1, no+1):
    for j in range(1, no + 1):
        if G[i][j] != 100:
            Edge.append((i, j, G[i][j]))

# 가중치의 오름차순 정렬
Edge.sort(key=lambda x: x[2])

p = [x for x in range(no + 1)]  #부모를 자기 자신으로 설정
ans = cnt = 0
group = no  # 섬의 수
for u, v, w in Edge:
    a = find_set(u); b = find_set(v)
    if a != b:      # dis-joint set
        p[b] = a    # union
        ans, cnt, group = ans + w, cnt + 1, group - 1
        if cnt == no - 1: break

#tree 간선의 수는 정점 - 1
if group == 1: print(ans)
else: print(-1)
