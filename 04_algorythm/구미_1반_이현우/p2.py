import sys
sys.stdin = open('p2.txt')

T = int(input())

dx = [0, 0, 1, -1]
dy = [1,-1, 0, 0]

def perm(n,k, dis):
    global row_dis

    if n == k:
        if dis < row_dis:
            row_dis = dis
    else:
        if dis < row_dis:
            for i in range(k, len(snack)):
                snack[k], snack[i] = snack[i], snack[k]
                perm(6, k+1, dis + abs(robot[k][0]-snack[k][0])+ abs(robot[k][1] - snack[k][1]))
                snack[k], snack[i] = snack[i], snack[k]

for tc in range(1,T+1):
    N= int(input())
    val= [list(map(int, input().split())) for _ in range(10)]

    robot = []
    snack = []
    row_dis =20 * 6

    for i in range(10):
        for j in range(10):
            if val[i][j] == 9:
                robot.append([i,j])
            elif val[i][j] != 0:
                snack.append([i,j])

    perm(6,0,0)

    print('#{} {}' .format(tc, row_dis))