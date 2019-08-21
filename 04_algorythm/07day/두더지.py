def mole(q, w):
    global num

    print(num)
    if ternel[q][w] == 1 and check == 0:
        count += 1
        for a in range(4):
            x = q + dy[a]
            y = w + dx[a]
            if x >= 0 and y >= 0 and x < n and y <n:
                mole(x, y)
        num += 1

    else:
        w += 1
        if w > n:
            q += 1
            w = 0
            mole(q,w)
        mole(q,w)






import sys

sys.stdin = open('두더지.txt')

n = int(input())

ternel = [list(map(int, input().split())) for _ in range(n)]

check = [[0 for _ in range(n)] for _ in range(n)]

num = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
x = 0
y = 0
count = 0


mole(0, 0)