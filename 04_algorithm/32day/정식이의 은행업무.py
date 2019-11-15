import sys

sys.stdin = open('정식이의 은행업무.txt')

T = int(input())


def tranb(ar):
    a= len(ar)-1
    val = 0
    sq = 1
    while a >= 0:
        if ar[a] == 1:
            val += ar[a]*sq

        sq *=2
        a -= 1

    return val


def trant(ar):
    a = len(ar) - 1
    val = 0
    sq = 1
    while a >= 0:
        if ar[a] != 0:
            val += ar[a] * sq

        sq *= 3
        a -= 1

    return val

def ranb(ar):
    for i in range(len(ar)):
        if ar[i] == 1:
            ar[i] = 0
            b.append(tranb(ar))
            ar[i] = 1

        else:
            ar[i] = 1
            b.append(tranb(ar))
            ar[i] = 0

def rant(ar, flag):
    if flag == 1:
        t.append(trant(ar))

    else:
        for i in range(len(ar)):
            if ar[i] == 0:
                ar[i] = 1
                rant(ar, 1)
                ar[i] = 2
                rant(ar,1)
                ar[i] = 0
            elif ar[i] == 1:
                ar[i] = 0
                rant(ar, 1)
                ar[i] = 2
                rant(ar,1)
                ar[i] = 1
            else:
                ar[i] = 0
                rant(ar, 1)
                ar[i] = 1
                rant(ar,1)
                ar[i] = 2


for tc in range(1, T+1):

    bin = list(map(int,input()))
    tri = list(map(int, input()))

    binlist =[]
    trilist = []

    b =[]
    t= []

    ranb(bin)
    rant(tri, 0)

    ans = 0

    for i in b:
        for j in t:
            if i == j :
                ans = j
                break
        if ans != 0:
            break

    print("#{} {}" .format(tc, ans))
