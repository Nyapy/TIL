import sys

sys.stdin= open('최소이동거리.txt')

T = int(input())

for tc in range(1,1+T):
    N, E =  map(int, input().split())

    sew = [list(map(int, input().split())) for _ in range(E)]

    arr = [[0 for _ in range(N+1)] for __ in range(N+1) ]


    for i in range(len(sew)):
        arr[sew[i][0]][sew[i][1]] = sew[i][2]
        arr[sew[i][1]][sew[i][0]] = sew[i][2]


    for i in range(N+1):
        for j in range(N+1):
            print(arr[i][j] , end = ' ')
        print()

    print(sew)