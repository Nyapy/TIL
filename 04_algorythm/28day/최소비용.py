import sys
import heapq
# import time
from time import strftime

# start_time = time.time()

sys.stdin = open('최소비용.txt')

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def mst(x,y):
    q = []
    l,r = 0, -1
    D[y][x] = 0
    ux = x
    uy = y
    # q.append([ux,uy,D[ux][uy]])

    heapq.heappush(heap, (D[y][x], y, x))


    while 1:
        min = 987654321

        # q.sort(key= lambda x: x[2])
        #
        # t = q.pop(0)
        #
        # ux = t[0]
        # uy = t[1]

        d, ux, uy = heapq.heappop(heap)

        visited[uy][ux] = 1

        for k in range(4):
            nx = ux + dx[k]
            ny = uy + dy[k]
            if nx >= 0 and ny >= 0 and nx < N and ny <N:
                if visited[ny][nx] == 0:
                    if height[ny][nx] > height[uy][ux] :
                        if D[ny][nx] > height[ny][nx]-height[uy][ux]+1+D[uy][ux] :
                            D[ny][nx] = height[ny][nx]-height[uy][ux]+1+D[uy][ux]
                            # q.append([nx,ny,D[ny][nx]])
                            heapq.heappush(heap, (D[ny][nx], nx, ny))

                    else :
                        if D[ny][nx] > 1+D[uy][ux] :
                            D[ny][nx] = 1+D[uy][ux]
                            # q.append([nx, ny, D[ny][nx]])
                            heapq.heappush(heap, (D[ny][nx], nx, ny))
        if ux == N-1 and uy == N-1:
            return


for tc in range(1,T+1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*(N) for _ in range(N)]
    D = [[1001*N for _ in range(N)] for __ in range(N)]
    heap = []

    mst(0,0)
    print('#{} {}' .format(tc, D[N-1][N-1]))

# print(time.time() - start_time, 'seconds')