import sys
sys.stdin = open('f.txt')

N, sor = input().split()

number = [list(map(int, input().split())) for _ in range(int(N))]

print(number)

vert = max(number)[0] * 2 - 1

ans = [[]] * vert

col = 0
while col < vert:
    for i in range(int(N)):
        row = number[i][0]
        print(row)
        for j in str(number[i][1]):
            if j == 1:
