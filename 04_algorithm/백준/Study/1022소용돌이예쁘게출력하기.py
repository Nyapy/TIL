import sys

sys.stdin = open("1022.txt")

r1,c1,r2,c2 = map(int, input().split())

num = max(map(abs, [r1,c1,r2,c2]))

dx = [1, 0, -1,0]
dy = [0, -1, 0,1]

soyong = [[0 for _ in range(num*2+1)] for _ in range(num*2+1)]

x = num
y = num
cnt = 1

flag = 0
n = 0

soyong[y][x] = 1

length = 1
while cnt <= ((num*2+1)**2):
    for i in range(length):
        nx = x + dx[n]
        ny = y + dy[n]
        cnt += 1
        soyong[ny][nx] = cnt

        if cnt == ((num*2+1)**2):
            break

        x = nx
        y = ny
    if cnt == ((num*2+1)**2):
        break
    flag += 1

    if flag == 2:
        flag = 0
        length += 1

    n = (n + 1) % 4

for i in range(num+r1,num+r2+1):
    for j in range(num+c1,num+c2+1):
        print("{}" .format(soyong[i][j]), end = " ")
    print()