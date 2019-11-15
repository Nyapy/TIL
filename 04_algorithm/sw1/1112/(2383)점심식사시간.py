def dist(p, s):
    return abs(man[p][0] - stair[s][0]) + abs(man[p][1] - stair[s][1])

import sys
sys.stdin = open("(2383)점심식사시간_input.txt")
MAXTIME = 10 * 2 + 10 * 10 # 4 ≤ N ≤ 10, 1 ≤ 사람의 수 ≤ 10, 2 ≤ 계단의 길이 ≤ 10
T = int(input())
for tc in range(1, T + 1):
    N = int(input())     #방의 한 변의 길이 N (4 ≤ N ≤ 10)
    man, stair = [], []  # 사람 좌표, (계단 좌표, 길이)

    MAP = []
    for i in range(N):
        MAP.append(list(map(int, input().split())))
        for j in range(N):
            if MAP[i][j] == 1:
                man.append((i, j))  # 사람 좌표
            elif MAP[i][j] > 1:
                stair.append((i, j, MAP[i][j])) # 계단 좌표, 길이

    P = len(man)    # 사람수

    ans = 0xfffffff

    for i in range(1 << P):  # 부분집합
        maxTime = 0
        # 0, 1 번 계단의 도착시간별 사람 수 카운팅
        arrive = [[0] * 21 for _ in range(2)]

        for j in range(P):
            if i & (1 << j):
                arrive[1][dist(j, 1) + 1] += 1
            else:
                arrive[0][dist(j, 0) + 1] += 1

        # 0, 1 번 계단 내려 가는 시간 계산
        for k in range(2):
            # 시간대별 계단에 있는 사람의 인원
            onstair = [0] * MAXTIME
            # 시간별
            for time in range(21):  # 시간대별 시뮬레이션
                while arrive[k][time] > 0:
                    arrive[k][time] -= 1 # 카운터 감소
                    now = time
                    while now < MAXTIME:
                        if onstair[now] < 3: break
                        now += 1  # 3명이상이면 시간 +1 증가
                    for move in range(now, now + stair[k][2]):  # 현재 time부터 깊이까지
                        onstair[move] += 1      #시간대별 인원 카운팅
                    maxTime = max(maxTime, now + stair[k][2])
        ans = min(ans, maxTime)
    print('#{} {}'.format(tc, ans))
