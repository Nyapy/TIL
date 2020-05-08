import sys

sys.stdin = open('5648.txt')

dx = [0,0,-0.5,0.5]
dy = [0.5,-0.5,0,0]

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    atoms = [list(map(int,input().split())) for _ in range(N)]
    # print(atoms)
    energy = 0

    extin = [0] * N
    flag = 1
    while flag:
        check = dict()
        for i in range(N):
            if not extin[i]:
                x,y,k,e = atoms[i]
                nx, ny = x+dx[k], y+dy[k]
                atoms[i] = [nx,ny,k,e]

                if nx > 1000 or nx <-1000 or ny > 1000 or ny <-1000:
                    extin[i] = 1
                else:
                    if check.get((nx,ny)):
                        check.get((nx,ny)).append(i)
                    else:
                        check[(nx,ny)] = [i]


        for j in check.values():
            if len(j) >=2 :
                for k in j:
                    energy += atoms[k][3]
                    extin[k] = 1
        flag = 0
        for k in range(N):
            if extin[k] == 0:
                flag = 1
                break

    print("#{} {}" .format(tc, energy))