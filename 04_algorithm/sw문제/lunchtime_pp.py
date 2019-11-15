import sys

sys.stdin = open('lunchtime.txt')

def cal():
    global ret
    tt = list(visit)
    for i in range(len(tt)):
        tt[i] = [pl[i][tt[i]], tt[i]]
    tm = 0
    st = [[], []]
    pc = 0
    while pc != pec and tm < ret:
        tm += 1
        for t in tt:
            t[0] -= 1
            if t[0] == 0:
                st[t[1]].append(s[t[1]][2])
        for i in range(2):
            for j in range(len(st[i])):
                if j == 3:
                    break
                st[i][j] -= 1
        for i in range(2):
            for j in range(len(st[i]) - 1, -1, -1):
                if st[i][j] == 0:
                    st[i].pop(j)
                    pc += 1
    ret = min(tm, ret)

def sol(x):
    cal()
    for i in range(x, len(pl)):
        if visit[i] == 0:
            visit[i] = 1
            sol(i + 1)
            visit[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    people = []
    s = []
    pec = 0
    for y in range(N):
        for x in range(N):
            if m[y][x] == 1:
                people.append([y, x])
                pec += 1
            elif m[y][x] > 1:
                s.append([y, x, m[y][x]])
    pl = []
    ret = 999
    visit = [0 for _ in range(pec)]
    for i in people:
        pl.append([abs(i[0] - s[0][0]) + abs(i[1] - s[0][1]), abs(i[0] - s[1][0]) + abs(i[1] - s[1][1])])
    sol(0)
    print("#{} {}".format(tc, ret + 2))