import sys

sys.stdin = open('단순 2진 암호코드.txt')

T = int(input())

n0 = [0,0,0,1,1,0,1]
n1 = [0,0,1,1,0,0,1]
n2 = [0,0,1,0,0,1,1]
n3 = [0,1,1,1,1,0,1]
n4 = [0,1,0,0,0,1,1]
n5 = [0,1,1,0,0,0,1]
n6 = [0,1,0,1,1,1,1]
n7 = [0,1,1,1,0,1,1]
n8 = [0,1,1,0,1,1,1]
n9 = [0,0,0,1,0,1,1]

def amho():
    global imi
    for i in range(N):
        for j in range(M-1,-1,-1):
            if arr[i][j] == 1:
                imi = arr[i][j-55:j+1]
                return

def trans(tem):
    if tem == n0:
        return 0
    elif tem == n1:
        return 1
    elif tem == n2:
        return 2
    elif tem == n3:
        return 3
    elif tem == n4:
        return 4
    elif tem == n5:
        return 5
    elif tem == n6:
        return 6
    elif tem == n7:
        return 7
    elif tem == n8:
        return 8
    elif tem == n9:
        return 9


for tc in range(1,1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    amho()
    imitation = []

    for i in range(0,len(imi),7):
        tem = imi[i:i+7]
        a=trans(tem)
        imitation.append(a)

    check = 0
    for i in range(0,len(imitation)-1,2):
        check += imitation[i]*3
    for j in range(1, len(imitation)-1, 2):
        check += imitation[j]
    check += imitation[-1]

    ans = 0
    if check % 10 == 0:
        for k in imitation:
            ans += k

    else :
        ans = 0

    print('#{} {}' .format(tc, ans))
