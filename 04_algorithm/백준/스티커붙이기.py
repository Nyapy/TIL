import sys

sys.stdin = open("스티커붙이기.txt")

N,M,K = map(int, input().split())

notebook = [[0 for _ in range(M)] for _ in range(N)]

stickers = []

def check(R,C,tem):

    if N-R+1 <= 0 or M-C+1 <= 0:
        return 0

    for i in range(N-R+1):
        for j in range(M-C+1):
            flag = 1
            for k in range(R):
                for l in range(C):
                    if tem[k][l] == 1 :
                        if notebook[i+k][j+l] == 1:
                            flag = 0
            if flag:
                A = i
                B = j
                break
        if flag:
            break
    if flag:
        for i in range(R):
            for j in range(C):
                if tem[i][j] == 1:
                    notebook[A+i][B+j] = 1
        return 1
    else:
        return 0

def change(tem,n):
    if n == 1:
        ntem = []
        for j in range(C):
            t = []
            for i in range(R-1,-1,-1):
                t.append(tem[i][j])
            ntem.append(t)

    elif n == 2:
        ntem = []
        for i in range(R-1,-1,-1):
            t = []
            for j in range(C-1,-1,-1):
                t.append(tem[i][j])
            ntem.append(t)
    elif n == 3 :
        ntem = []
        for j in range(C-1,-1,-1):
            t = []
            for i in range(R):
                t.append(tem[i][j])
            ntem.append(t)
    return ntem

for _ in range(K):
    R,C = map(int, input().split())
    tem = []
    for j in range(R):
        tem.append(list(map(int, input().split())))

    f = 0
    f = check(len(tem), len(tem[0]), tem)
    for z in range(1,4):
        if f == 0:
            ntem = change(tem,z)
            f = check(len(ntem), len(ntem[0]), ntem)

cnt = 0
for i in range(N):
    for j in range(M):
        if notebook[i][j] == 1:
            cnt +=1

print(cnt)


