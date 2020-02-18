import sys
sys.stdin = open("17406.txt")


from collections import deque
N,M,K = map(int, input().split())

oriarray = [0]+[[0]+list(map(int, input().split())) for _ in range(N)]

array = [[0 for _ in range(M+1)] for _ in range(N+1)]

rcs = [list(map(int, input().split())) for _ in range(K)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]



result = 987654321
def perm(n,k):
    if n == k:
        rotation()
        # print(rcs)
    else:
        for i in range(k,n):
            rcs[k],rcs[i] = rcs[i],rcs[k]
            perm(n,k+1)
            rcs[k],rcs[i] = rcs[i],rcs[k]


def rotation():
    global result
    for i in range(1,N+1):
        for j in range(1,M+1):
            array[i][j] = oriarray[i][j]

    for i in range(K):
        visited = [[0 for _ in range(M+1)] for _ in range(N+1)]
        r,c,s = rcs[i][0],rcs[i][1],rcs[i][2]

        lux , luy = c-s,r-s
        rux, ruy = c+s,r+s
        q= deque()
        while lux != rux or luy != ruy:
            q.append([lux,luy])

            k = 0
            before = array[luy][lux]

            while q:
                t = q.popleft()
                x, y = t[0],t[1]

                nx, ny = x+dx[k], y+dy[k]

                if lux<=nx<=rux and luy<=ny<=ruy:
                    pass

                else:
                    k += 1
                    if k ==4:
                        break
                    nx, ny = x + dx[k], y + dy[k]

                if visited[ny][nx] == 0:
                    tem = array[ny][nx]
                    array[ny][nx] = before
                    before = tem
                    visited[ny][nx] = 1
                    q.append([nx, ny])
            lux += 1
            luy += 1
            rux -= 1
            ruy -= 1
    for i in range(1,N+1):
        tem=0
        for j in range(1,M+1):
            tem += array[i][j]

        if result >tem:
            result = tem

perm(K,0)

print(result)