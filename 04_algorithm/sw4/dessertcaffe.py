import sys

sys.stdin = open('dessertcaffe.txt')

T = int(input())

def calc(x,y,l,r):
    visited = [0] * 101
    total = 0
    for i in range(1,l+1):
        for j in range(1,r+1):
            if visited[G[y+i][x-i]] == 1:
                return -1
            total += G[y+i][x-i]
            visited[G[y+i][x-i]] =1

            if visited[G[y+j][x+j]] == 1:
                return -1
            total += G[y + j][x + j]
            visited[G[y+j][x+j]] = 1

            if visited[G[y+l+j][x+l-j]] == 1:
                return -1
            total += G[y + j][x + j]
            visited[G[y+l+j][x+l-j]] = 1

            if visited[G[y+r+i][x+r-l]] == 1:
                return -1
            total += G[y+r+i][x+r-l]
            visited[G[y+r+i][x+r-l]] = 1

    return total


for tc in range(1,T+1):
    N = int(input())

    G = [list(map(int, input().split())) for _ in range(N)]

    mv = 0

    for i in range(N-2):
        for j in range(1,N-1): #시작점 선택

            if j <= N - i - 1:
                a = j
            else:
                a = N - i - 1

            if N - i - 1 <= N - j -1:
                b = N - i - 1
            else:
                b = N - j- 1

            for ld in range(1, a+1):
                for rd in range(1, b+1):
                    val = calc(j,i,ld,rd)
                    if val != -1:
                        if val > mv :
                            mv = val

    print(mv)
