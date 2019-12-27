import sys

sys.stdin = open("1600말이되고픈원숭이.txt")

K = int(input())

W, H = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(H)]

result = 987654321
dx = [0,0,-1,1]
dy = [-1,1,0,0]

hx = [-2,-1,1,2,-2,-1,1,2]
hy = [-1,-2,-2,-1,1,2,2,1]

visited = [[[999999999 for _ in range(W)] for _ in range(H)] for _ in range(K+1)]

def monkey(x,y, dist, hmove):
    global result
    if dist > result:
        return

    visited[hmove][y][x] = dist
    q = []
    q.append([x,y,dist])

    while q:
        t= q.pop(0)
        dist = t[2]

        for k in range(4):
            nx = t[0] + dx[k]
            ny = t[1] + dy[k]

            if 0 <= nx < W and 0 <= ny < H and visited[hmove][ny][nx] == 999999999 and board[ny][nx] == 0:
                if nx == W-1 and ny == H-1:
                    if result > dist:
                        result = dist
                    visited[hmove] = [[999999999 for _ in range(W)] for _ in range(H)]
                    return
                q.append([nx,ny,dist+1])
                visited[hmove][ny][nx] = dist +1

        if hmove < K:
            for k in range(8):
                nx = t[0] + hx[k]
                ny = t[1] + hy[k]
                if 0 <= nx < W and 0 <= ny < H and visited[hmove][ny][nx] == 999999999and board[ny][nx] == 0:
                    if nx == W - 1 and ny == H - 1:
                        if result > dist:
                            result = dist
                        visited[hmove] = [[999999999 for _ in range(W)] for _ in range(H)]
                        return

                    monkey(nx,ny, dist+1, hmove+1)

    visited[hmove] = [[999999999 for _ in range(W)] for _ in range(H)]
    return -1

monkey(0,0,1,0)

if result == 987654321:
    result = -1



print(result)