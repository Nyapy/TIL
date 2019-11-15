import sys
import time

start = time.time()
sys.stdin = open('p3.txt')

T = int(input())

def perm(n,k, totalm, energy):
    global  max_mineral
    if totalm > max_mineral:
        max_mineral = totalm

    if energy <= 0:
        return

    if n == k:
        return

    else:
        for i in range(k, n):
            mineral[i], mineral[k] = mineral[k], mineral[i]
            a = energy - (abs(mineral[k][0] - robot0) + abs(mineral[k][1] - robot1))*2
            if a >= 0:
                perm(n, k+1, totalm + mineral[k][2], a)
            elif a < 0:
                return
            mineral[i], mineral[k] = mineral[k], mineral[i]

for tc in range(1,T+1):
    N,M,C = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]

    max_mineral = 0

    robot = []
    mineral = []
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                robot += [i,j]

            elif ground[i][j] != 0:
                mineral.append([i,j, ground[i][j]])
    robot0 = robot[0]
    robot1 = robot[1]
     # mineral.sort(key= lambda x: abs(x[0]-robot[0])+abs(x[1]-robot[1]))
    # print(mineral)
    perm(len(mineral), 0, 0, C)

    print('#{} {}' .format(tc, max_mineral))
    print('{}' .format(time.time()-start))