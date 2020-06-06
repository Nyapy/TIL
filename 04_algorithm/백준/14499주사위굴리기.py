import sys

sys.stdin= open("14499.txt")

N,M,y,x,K = map(int, input().split())

G = [list(map(int, input().split())) for _ in range(N)]

go = list(map(int, input().split()))
dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]
dice_num = [0]*7
dice = list(range(7))

for k in go:
    nx, ny = x + dx[k], y + dy[k]
    if 0 <= nx < M and 0 <= ny < N:
        if k == 1:
            dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
        elif k == 2:
            dice[1], dice[4], dice[6], dice[3] = dice[3], dice[1], dice[4], dice[6]
        elif k == 3:
            dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]
        elif k == 4:
            dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]

        if G[ny][nx] == 0:
            G[ny][nx] = dice_num[dice[6]]
        else:
            dice_num[dice[6]] = G[ny][nx]
            G[ny][nx] = 0

        x, y = nx, ny
        print(dice_num[dice[1]])

    else:
        pass

# for i in range(K):
#     go[i] -= 1
#
# nextnum = [[],[1,2,3,5,4],[2,6,3,1,4],[3,2,6,5,1],[4,2,1,5,6],[5,1,3,6,4],[6,5,3,2,4]]
# nextdirec = [[],[0,0,0,0,0],[0,0,3,0,1],[0,1,2,3,0],[0,3,0,1,3],[0,0,1,0,3],[0,0,2,0,2]]
#
# direc = 0
# up = 1
# down = 6
#
# print(go)
#
# for i in range(K):
#     up = nextnum[up][(go[i]-direc+4)%4]
#     direc = nextdirec[up]