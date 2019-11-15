def dfs(no, energy, cnt):                  # 정류장번호, 남은용량, 교체횟수
    global min
    if no >= arr[0]:                        # 종점에 다다른 경우
        if min > cnt:
            min = cnt
    else:
        if energy > 0:
            dfs(no + 1, energy - 1, cnt)   # 교체하지 않고 통과
        if cnt < min:
            dfs(no + 1, arr[no] - 1, cnt + 1)    # 교체

import sys
sys.stdin = open('(5208)전기버스2_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):          
    arr = list(map(int, input().split()))       # 정류장 수, 충전지 용
    min = 987654321
    dfs(2, arr[1]-1, 0)                        # 2번 정류장일 때 1번 정류장에서 충전량에서 -1 함
    print('#{} {}'.format(tc, min))

