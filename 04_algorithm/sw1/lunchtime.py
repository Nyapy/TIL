import sys

sys.stdin = open('lunchtime.txt')

T = int(input())

def group(n,k):
    if n == k :
        seq = []
        for i in range(n):
            if groups[i] == 1:
                gotostair(P[i],S[0],seq,0)
            else:
                gotostair(P[i],S[1],seq,1)
        seq.sort(key=lambda x: x[2])
        # print(seq)

        timeflow(seq)

    else:
        groups[k] = 0
        group(n, k+1)
        groups[k] = 1
        group(n, k+1)

def timeflow(seq):
    global Time
    q0 = []
    q1 = []
    t = 0
    while seq or q0 or q1 :
        if t >= Time :
            return
        if q0 :
            if len(q0) > 3 :
                for i in range(3):
                    q0[i] -= 1
                while q0[0] == 0:
                    q0.pop(0)

            elif len(q0) > 0:
                for i in range(len(q0)):
                    q0[i] -= 1
                while q0 and q0[0] == 0:
                    q0.pop(0)
        if q1 :
            if len(q1) > 3 :
                for i in range(3):
                    q1[i] -= 1
                while q1[0] == 0:
                    q1.pop(0)
            elif len(q1) > 0:
                for i in range(len(q1)):
                    q1[i] -= 1
                while q1 and q1[0] == 0:
                    q1.pop(0)
        if seq:
            while seq and seq[0][2] == t:
                a = seq.pop(0)
                if a[3] == 0:
                    q0.append(S[0][2])
                else :
                    q1.append(S[1][2])

        t += 1
    Time = t
    return Time


def gotostair(p,g,seq,m):
    t = abs(p[0]-g[0])+ abs(p[1]-g[1])
    seq.append(p+[t,m])


for tc in range(1, T+1):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]
    Time = 10000

    # print(G)


    P = []
    S = []

    for i in range(N):
        for j in range(N):
            if G[i][j] == 1:
                P.append([j,i])
            elif G[i][j] > 1 :
                S.append([j,i,G[i][j]])
    # print(P)

    pnum = len(P)
    groups = [0]*pnum

    group(pnum,0)

    print('#{} {}' .format(tc, Time))