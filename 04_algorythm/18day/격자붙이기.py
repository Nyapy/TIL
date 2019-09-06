import sys

sys.stdin = open('격자붙이기.txt')

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def seven(x,y,c,tem):
    tem += grid[y][x]
    if c == 6:
        numbers.add(tem)
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >= 0 and ny >= 0 and nx < 4 and ny < 4:
            seven(nx,ny,c+1,tem)


for tc in range(1, 1+T):
    grid = [list(input().split()) for _ in range(4)]
    check = [[[]]*4 for __ in range(4)]
    visited = [[0 for _ in range(4)] for _ in range(4)]

    numbers = set()

    q = []

    for i in range(4):
        for j in range(4):
            c= 0
            tem = ''
            seven(i,j,c, tem)


    print('#{} {}' .format(tc, len(numbers)))