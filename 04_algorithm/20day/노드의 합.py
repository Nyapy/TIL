import sys

sys.stdin = open('노드의 합.txt')

T = int(input())

for tc in range(1,T +1):
    N,M,L = map(int, input().split())
    leap = [list(map(int, input().split())) for _ in range(M)]

    tem = [0] * (N+1)
    for i in range(len(leap)):
        tem[leap[i][0]] = leap[i][1]

    if len(tem) %2 == 0:
        for i in range(len(tem)//2-1, 0, -1):
            tem[i] = tem[i*2]+ tem[i*2+1]

    elif len(tem)%2 == 1:
        tem[len(tem)//2] = tem[(len(tem)//2)*2]
        for i in range(len(tem)//2-1, 0, -1):
            tem[i] = tem[i*2]+ tem[i*2+1]

    print(tem)

    print('#{} {}' .format(tc, tem[L]))