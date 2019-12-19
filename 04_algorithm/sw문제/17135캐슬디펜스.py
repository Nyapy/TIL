import sys

sys.stdin = open("17135.txt")

N, M, D = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

bow = [0 for _ in range(M)]

result = 0


def comb(n,k):
    if M-n < 3-k:
        return
    if k == 3:
        tem = [[0 for _ in range(M)] for _ in range(N)]
        defence(tem)
        return
    else:
        bow[n] = 1
        comb(n+1, k+1)
        bow[n] = 0
        comb(n+1, k)

def defence(tem):
    global result
    kill = 0
    last = N
    while last > 0:
        target = [[M,N,N+M+1] for _ in range(M)]
        for i in range(last-1,-1,-1):
            for j in range(M):
                if board[i][j] and tem[i][j]== 0:

                    for k in range(M):
                        if bow[k] == 1:
                            dist = last-i + abs(k-j)
                            if dist <= D:
                                if target[k][2] > dist: ####################### 이 부분 함정
                                    target[k] = [j,i,dist]
                                elif target[k][2] == dist:
                                    if target[k][0] > k:
                                        target[k] = [j,i,dist]
        kill_target = []

        for tar in target:
            flag = True
            if tar[2] != N+M+1:
                for kil in kill_target:
                    if kil[0] == tar[0] and kil[1] == tar[1]:
                        flag = False;
                        break;
                if flag:
                    kill_target.append(tar);



        for zegu in kill_target:
            tem[zegu[1]][zegu[0]] = 1
            kill += 1

        last -= 1

    if result < kill:
        result = kill

comb(0,0)

print(result)