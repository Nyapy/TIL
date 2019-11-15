import sys
sys.stdin = open("(4013)특이한 자석_input.txt")
T = int(input())
SIZE = 4
for tc in range(1, T+1):
    N, S = 0, 1
    K = int(input())
    num, dir = 0 , 0
    move = []    # 1:시계, -1:반시계 방향
    mt = [list(map(int, input().split())) for _ in range(4)]

    for i in range(K):
        num, dir = map(int, input().split())  # 자석번호, 회전방향
        move = [0] * 4  # 초기화 주의
        move[num-1] = dir

        # 왼쪽편
        a = b = 0
        for j in range(num - 1, 0, -1):
            if mt[j][6] == 1: a = 1  # 앞
            else: a = 0

            if mt[j - 1][2] == 1: b = 1  # 뒤
            else: b = 0

            if a == b : break
            if move[j] == 1: move[j-1] = -1
            elif move[j] == -1: move[j-1] = 1

        # 오른쪽편
        for j in range(num - 1, 3):
            if mt[j][2] == 1: a = 1  #앞
            else: a = 0

            if mt[j+1][6] == 1: b = 1 #뒤
            else: b = 0

            if a == b : break
            if move[j] == 1: move[j+1] = -1
            else: move[j+1] = 1

        # shift
        for j in range(0, 4):
            if move[j] == 0: continue
            if move[j] == 1:    # 맨뒤 맨앞으로
                tmp = mt[j][7]
                for k in range(6, -1, -1):
                    mt[j][k+1] = mt[j][k]
                mt[j][0] = tmp
            else:               # 맨앞 맨뒤로
                tmp = mt[j][0]
                for k in range(1, 8):
                    mt[j][k-1] = mt[j][k]
                mt[j][7] = tmp

    ans = 0
    for i in range(3, -1, -1):
        ans = ans * 2 + mt[i][0]

    print("#{} {}".format(tc, ans))
