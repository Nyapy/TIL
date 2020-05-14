import sys
sys.stdin = open("2382.txt")

def Print(dict):
    for i in range(N):
        for j in range(N):
            if (i, j) in virus:
                print(virus[(i, j)], end=' ')
            else:
                print([0, 0], end=' ')
        print("")
    print("")


def calc(dict):
    total = 0
    for rc, val in dict.items():
        total += val[NUM]
    return total


# SWEA 2382. 미생물 격리
def solve():
    global virus
    for _ in range(M):
        new = {}  # 이동을 마친 바이러스

        # 이동
        for rc, val in virus.items():
            num, direct, _ = val
            next_row = rc[0] + dx[direct - 1]
            next_col = rc[1] + dy[direct - 1]
            if next_row == 0 or next_row == N - 1 or next_col == 0 or next_col == N - 1:
                if direct == 1:
                    direct = 2
                elif direct == 2:
                    direct = 1
                elif direct == 3:
                    direct = 4
                elif direct == 4:
                    direct = 3
                num = num // 2
                if num == 0:
                    continue

            if (next_row, next_col) not in new:
                new[(next_row, next_col)] = [num, direct, num]
            else:
                if num > new[(next_row, next_col)][MAX]:  # 맥스 num보다 크면 direct를 교체
                    new[(next_row, next_col)][DIRECT] = direct
                    new[(next_row, next_col)][MAX] = num  # max 교체
                new[(next_row, next_col)][NUM] += num
            '''
            # 합치기
            if next_row in new:
                if next_col in new[next_row]:  # 이미 같은 셀에 군집이 존재함
                    if num > new[next_row][next_col][MAX]:  # 맥스 num보다 크면 direct를 교체
                        new[next_row][next_col][DIRECT] = direct
                        new[next_row][next_col][MAX] = num  # max 교체

                    new[next_row][next_col][NUM] += num
                else:  # row는 있지만 해당 col은 없음. 그냥 추가 (1)
                    new[next_row][next_col] = [num, direct, num]  # 같은 셀에 중복되는 군집 없으므로 자신이 max가 됨
            else:  # row 없음. 그냥 추가 (2)
                new[next_row] = {next_col: [num, direct, num]}  # 같은 셀에 중복되는 군집 없으므로 자신이 max가 됨
            '''
            virus = new
    return calc(virus)


NUM, DIRECT, MAX = 0, 1, 2
T = int(input())
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
for i in range(T):
    N, M, K = map(int, input().split())  # 격자의 크기 N, 시간 M, 군집의 갯수 K
    virus = {}
    for _ in range(K):
        x, y, n, d = map(int, input().split())  # 가로, 세로, 군집크기, 방향

        virus[(x, y)] = [n, d, n]  # 군집 크기, 방향, max(같은 셀에 모인 군집 중 가장 큰 크기. 현재는 자기 뿐이므로 자기 자신의 크기 n)

    print("#{} {}".format(i + 1, solve()))