import sys

sys.stdin = open("1022.txt")

r1,c1,r2,c2 = map(int, input().split())

dx = [1, 0, -1,0]
dy = [0, -1, 0,1]

soyong = [[0 for _ in range(10002)] for _ in range(10002)]

x = 5000
y = 5000
cnt = 1

flag = 0
n = 0

length = 1
while cnt <= 100000000:
    for i in range(length):
        nx = x + dx[n]
        ny = y + dy[n]
        cnt += 1
        soyong[ny][nx] = cnt

        if cnt == 100000000:
            break

        x = nx
        y = ny
    if cnt == 100000000:
        break
    flag += 1

    if flag == 2:
        flag = 0
        length += 1

    n = (n + 1) % 4

for i in range(5000-r1,5000+r2):
    for j in range(5000-c1,5000+c2):
        print(soyong[i][j], end = " ")
    print()