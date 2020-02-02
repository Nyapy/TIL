import sys

sys.stdin = open("2823.txt")

R, C = map(int, input().split())

street = [list(input()) for _ in range(R)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

flag = 0

for i in range(R):
    for j in range(C):
        if street[i][j] == '.':
            poten = 0
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if 0 <= nx < C and 0 <= ny < R and street[ny][nx]== '.':
                    poten += 1
            if poten <= 1:
                flag = 1

        if flag :
            break
    if flag :
        break

print(flag)