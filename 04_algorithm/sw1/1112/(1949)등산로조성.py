def dfs(cur_r, cur_c, cur_height, cur_used, cur_len):
    global ans

    if ans < cur_len:
        ans = cur_len # 길이 비교

    for i in range(4):  # 4방향
        nxt_used, nxt_len = cur_used, cur_len
        nxt_r = cur_r + dy[i]
        nxt_c = cur_c + dx[i]

        # 인덱스 체크
        if nxt_r < 0 or nxt_r >= N or nxt_c < 0 or nxt_c >= N:continue
        nxt_height = arr[nxt_r][nxt_c]

        # 방문여부 체크
        if visit[nxt_r][nxt_c] : continue

        if nxt_height < cur_height:  # 다음높이가 현재 높이보다 낮다
            visit[nxt_r][nxt_c] = 1
            nxt_len += 1
            dfs(nxt_r, nxt_c, nxt_height, nxt_used, nxt_len)
            visit[nxt_r][nxt_c] = 0
        else : #다음높이가 현재 높이보다 높거나 같다
            if cur_used == 0 and nxt_height - K < cur_height:
                visit[nxt_r][nxt_c] = 1
                nxt_len += 1
                nxt_used = 1
                nxt_height = cur_height - 1 # 높은지형에서 낮은지형을 가야함으로 1차이만큼만 깎음
                dfs(nxt_r, nxt_c, nxt_height, nxt_used, nxt_len)
                visit[nxt_r][nxt_c] = 0

import sys
sys.stdin = open("(1949)등산로조성_input.txt")
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(T):
    # 지도의 크기(3 ≤ N ≤ 8), 최대 공사 깊이(1 ≤ K ≤ 5)
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    ans = 0
    #현재 행, 열, 높이, 사용여부, 길이
    cur_r, cur_c, cur_height, cur_used, cur_len = 0,0,0,0,0

    #최대값 구하기(① 등산로는 가장 높은 봉우리에서 시작해야 한다.)
    highest = 0
    for i in range(N):
        for j in range(N):
            if highest < arr[i][j]: highest = arr[i][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == highest:
                visit[i][j] = 1
                cur_r, cur_c, cur_height, cur_used, cur_len = i, j, arr[i][j], 0, 1
                dfs(cur_r, cur_c, cur_height, cur_used, cur_len)
                visit[i][j] = 0

    print("#{} {}".format(tc+1, ans))