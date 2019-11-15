import sys

sys.stdin = open('specialmagnet.txt')

T = int(input())


def rotation(g, rot):
    visited[g] = 1
    q = []
    left = []
    right = []
    q.append([g,rot])
    if rot == 1:
        right.append(g)
    else :
        left.append(g)

    while q:
        t = q.pop(0)
        gearnum = t[0]
        rotdi = t[1]

        for i in [-1,1]:
            ngearnum = t[0]+i

            if 0<= ngearnum <4:
                if visited[ngearnum] == 0:
                    if i == -1:
                        if nal[ngearnum][LR[ngearnum][1]] != nal[gearnum][LR[gearnum][0]]:
                            if rotdi == -1:
                                right.append(ngearnum)
                                visited[ngearnum] = 1
                                q.append([ngearnum, 1])
                            else:
                                left.append(ngearnum)
                                visited[ngearnum] = 1
                                q.append([ngearnum, -1])


                    elif i == 1:
                        if nal[ngearnum][LR[ngearnum][0]] != nal[gearnum][LR[gearnum][1]]:
                            if rotdi == -1:
                                right.append(ngearnum)
                                visited[ngearnum] = 1
                                q.append([ngearnum, 1])
                            else:
                                left.append(ngearnum)
                                visited[ngearnum] = 1
                                q.append([ngearnum, -1])

    for a in range(len(left)):
        for z in range(3):
            LR[left[a]][z] += 1
            if LR[left[a]][z] == 8:
                LR[left[a]][z] = 0

    for a in range(len(right)):
        for z in range(3):
            LR[right[a]][z] -= 1
            if LR[right[a]][z] == -1:
                LR[right[a]][z] = 7

for tc in range(1,1+T):
    K = int(input())

    nal = [list(map(int, input().split())) for _ in range(4)]

    rotate = [list(map(int, input().split())) for _ in range(K)]

    LR = [[6,2,0] for _ in range(4)]

    # print(LR)
    point = 0
    for a in range(len(rotate)):
        visited = [0]*4
        rotation(rotate[a][0]-1, rotate[a][1])

    for i in range(len(nal)):
        if i == 0:
            if nal[i][LR[i][2]] == 1:
                point += 1

        elif i == 1:
            if nal[i][LR[i][2]] == 1:
                point += 2

        elif i == 2:
            if nal[i][LR[i][2]] == 1:
                point += 4

        elif i == 3:
            if nal[i][LR[i][2]] == 1:
                point += 8

    print("#{} {}" .format(tc, point))
