import sys

sys.stdin = open("14891.txt")

topni = [0]+[list(map(int, input())) for _ in range(4) ]

K = int(input())

rot = [list(map(int, input().split())) for _ in range(K) ]


n26 = [0]+ [[0,2,6] for _ in range(4)]

def rotation(num, d):
    visited[num] = 1
    for i in [-1,1]:
        if 0 < num + i <=4:
            if i == -1:
                if topni[num][n26[num][2]] != topni[num+i][n26[num+i][1]] and visited[num+i] == 0:
                    rotation(num+i, d*-1)
            else:
                if topni[num][n26[num][1]] != topni[num+i][n26[num+i][2]] and visited[num+i] == 0:
                    rotation(num+i, d*-1)
    if d == -1:
        for j in range(3):
            n26[num][j] = (n26[num][j]+1)%8
    else:
        for j in range(3):
            n26[num][j] = (n26[num][j]+7)%8

for i in range(K):
    visited = [0]*5
    rotation(rot[i][0], rot[i][1])

result = 0
for j in range(1,5):
    if topni[j][n26[j][0]] == 1:
        result += 2**(j-1)
print(result)