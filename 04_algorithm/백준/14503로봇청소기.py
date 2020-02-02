import sys

sys.stdin = open('14503.txt')
from collections import deque

N,M = map(int, input().split())
r,c,d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
visited = [[0 for _ in range(M)] for _ in range(N)]
def cleaning(r,c,d):
    clean = 0
    q = deque()
    q.append([c,r,d])
    while q:
        x,y,d = q.popleft()
        if visited[y][x] == 0:
            clean += 1
            visited[y][x] = clean
        flag = 1
        for i in range(1,5):
            nd = (d+4-i)%4
            nx = x + dx[nd]
            ny = y + dy[nd]
            if 0<=nx < M and 0 <= ny <N:
                if room[ny][nx] == 0 and visited[ny][nx] == 0:
                    q.append([nx,ny,nd])
                    flag = 0
                    break

        if flag:
            nx = x + dx[(d+2)%4]
            ny = y + dy[(d+2)%4]
            if 0<=nx < M and 0 <= ny <N:
                if room[ny][nx] == 0:
                    q.append([nx,ny,d])
                else:
                    break
    return clean
print(cleaning(r,c,d))