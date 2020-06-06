import sys
n = int(sys.stdin.readline())
apple = set([tuple(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline()))])
cmd = [list(sys.stdin.readline().split()) for i in range(int(sys.stdin.readline()))]
snake = [[-2]*n for _ in range(n)]
snake[0][0] = 0
x,y,d = 0,0,0
l = 1
t = 0
idx = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
# print((2,5) in apple)

while True:
    t += 1
    l += 1
    x += dx[d]
    y += dy[d]
    if x < 0 or x >= n or y < 0 or y >= n:
        break
    if snake[x][y] >= t-l+1:
        break
    if (x+1,y+1) in apple:
        apple.remove((x+1,y+1))
    else:
        l -= 1
    snake[x][y]=t

    if idx < len(cmd) and int(cmd[idx][0]) == t:
        if cmd[idx][1] == 'D':
            d = (d+1) % 4
        else:
            d = (d+3) % 4
        idx += 1
print(t)