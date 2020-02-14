import sys

sys.stdin = open("2151.txt")

N = int(input())

house = [list(input()) for _ in range(N)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]


doors = []
mirrors = []
check = [[0 for _ in range(N)] for _ in range(N)]

# print(check)
for i in range(N):
    for j in range(N):
        if house[i][j] == '!':
            mirrors.append([j,i])
        elif house[i][j] == '#':
            doors.append([j,i])

A = [0]*len(mirrors)

result = -1
def powerset(n,k, cnt):
    global result

    if result >= 0:
        return
    if k == n :
        for a in range(len(mirrors)):
            if A[a]:
                check[mirrors[a][1]][mirrors[a][0]] = A[a]

        flag = search(doors[0][0],doors[0][1])
        if flag:
            result = cnt

        for a in range(len(mirrors)):
            if A[a]:
                check[mirrors[a][1]][mirrors[a][0]] = 0

    else:
        A[k] = 0
        powerset(n,k+1,cnt)

        A[k] = 1
        powerset(n,k+1,cnt+1)
        A[k] = 2
        powerset(n, k + 1, cnt + 1)


def search(x,y):
    q = []
    for k in range(4):
        q.append([x,y,k,0])
    while q:
        t = q.pop(0)
        x =t[0]
        y =t[1]
        d =t[2]
        cnt = t[3]

        nx = x +dx[d]
        ny = y +dy[d]

        if 0 <= nx <N and 0 <= ny <N:
            if house[ny][nx] == '.':
                q.append([nx,ny,d,cnt])
            elif house[ny][nx] == '!':
                if check[ny][nx] == 1:
                    if d in [0,3]:
                        q.append([nx, ny, (d + 1) % 4, cnt + 1])
                    else:
                        q.append([nx, ny, (d + 3) % 4, cnt + 1])

                elif check[ny][nx] == 2:
                    if d in [0,3]:
                        q.append([nx, ny, (d + 3) % 4, cnt + 1])
                    else:
                        q.append([nx, ny, (d + 1) % 4, cnt + 1])

                elif check[ny][nx] == 0:
                    q.append([nx, ny, d, cnt])


            elif nx == doors[1][0] and ny == doors[1][1]:
                return 1
    return 0

powerset(len(mirrors),0,0)
print(result)