import sys
from collections import deque
from copy import deepcopy
from itertools import combinations
sys.stdin = open('5656.txt')

T = int(input())

N,W,H = map(int, input().split())

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def blockbreak(x,y):
    visited = [[0 for _ in range(W) for _ in range(H)]]
    visited[y][x] = 1

    q = deque()
    q.append([x,y])
    fx, fy = q.popleft()
    for k in range(4):
        tx, ty = fx, fy
        while visited[ty][tx]+1 <= copy_block[fy][fx]:
            nx , ny = tx + dx[k], ty + dy[k]
            if 0 <= nx < W and 0 <= ny < H :
                q.append([nx, ny])
                visited[ny][nx] = visited[ty][tx] + 1
                tx = nx
                ty = ny
            else:
                break
    for i in q:
        blockbreak(i[0],i[1])

def drop():
    next = []
    for j in range(H):
        tem = []
        for i in range(N):
            if block[i][j] :
                tem.append(block[i][j])

for tc in range(1, T+1):
    block = list(list(map(int, input().split())) for _ in range(H))

    copy_block = deepcopy(block)

    print(block)

