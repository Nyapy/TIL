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

visited = [[[-1 for _ in range(W)] for _ in range(H)] for _ in range(K+1)]

def monkey(x,y, dist, hmove):
    1
monkey(0,0,1,0)

if result == 987654321:
    result = -1



print(result)