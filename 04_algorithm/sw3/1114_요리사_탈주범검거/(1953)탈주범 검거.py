import sys
import collections
sys.stdin = open("(1953)탈주범 검거_input.txt")
T = int(input())

# 터널의 모양을 LIST에 저장 상하좌우
info = [[0,0,0,0],  # 0
        [1,1,1,1],  # 1
        [1,1,0,0],  # 2
        [0,0,1,1],  # 3
        [1,0,0,1],  # 4
        [0,1,0,1],  # 5
        [0,1,1,0],  # 6
        [1,0,1,0]]   # 7

#상하좌우
dy = [ -1, 1, 0, 0 ]
dx = [ 0, 0, -1, 1 ]

def solve(y, x):
    deq = collections.deque()
    deq.append([y, x])   #enQueue
    visit[y][x] = 1

    while len(deq) != 0:
        y, x = deq.popleft()   #deQueue  현재좌표

        if visit[y][x] >= L: return  # 길이(L) 보다 길면

        for i in range(4):
            ny = y + dy[i]  # 다음 좌표
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M: continue   # 벽 체크
            if visit[ny][nx] : continue
            if arr[ny][nx] == 0 : continue

            # 현재모양과 다음모양을 비교
            if i == 0 and info[arr[y][x]][0] == 1 and info[arr[ny][nx]][1] == 1 : # 상 == 하
                deq.append([ny, nx])
                visit[ny][nx] = visit[y][x] + 1
            elif i == 1 and info[arr[y][x]][1] == 1 and info[arr[ny][nx]][0] == 1 : # 하 == 상
                deq.append([ny, nx])
                visit[ny][nx] = visit[y][x] + 1
            elif i == 2 and info[arr[y][x]][2] == 1 and info[arr[ny][nx]][3] == 1: # 좌 == 우
                deq.append([ny, nx])
                visit[ny][nx] = visit[y][x] + 1
            elif i == 3 and info[arr[y][x]][3] == 1 and info[arr[ny][nx]][2] == 1: # 우 == 좌
                deq.append([ny, nx])
                visit[ny][nx] = visit[y][x] + 1


for tc in range(T):
    # 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 소요된 시간 L
    N, M, R, C, L = map(int, input().split())  #
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    ans = 0
    solve(R, C)

    for i in range(N):
        for j in range(M):
            if visit[i][j]:
                ans += 1

    print("#{} {}".format(tc+1, ans))

