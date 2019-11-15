import sys

sys.stdin = open('정사각형방.txt')

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def square(x,y):
    value = 0
    q = []
    l = 0

    visited[y][x] = 1
    q.append([x,y])

    while l < len(q):
        t = q[l]
        tx = t[0]
        ty = t[1]
        l+=1
        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[ny][nx] == arr[ty][tx]+1:
                    if visited[ty][tx]+1 > visited[ny][nx]:
                        visited[ny][nx] = visited[ty][tx] +1
                        q.append([nx,ny])
                        if value < visited[ny][nx]:
                            value = visited[ny][nx]
    return value\

for tc in range(1,T+1):
    N = int(input())
    visited = [[0 for _ in range(N)] for __ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(arr)

    visited = [[0 for _ in range(N)] for __ in range(N)]
    ans = 0
    a_x =0
    a_y = 0


    for i in range(N):
        for j in range(N):
            a= square(j,i)
            if ans < a :
                ans = a
                a_x = j
                a_y = i
            elif ans == a and arr[i][j] < arr[a_y][a_x]:
                a_x = j
                a_y = i

    print('#{} {} {}' .format(tc, arr[a_y][a_x], ans))