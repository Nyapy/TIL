import sys

sys.stdin = open('사람네트워크.txt')

T = int(input())

def floyd(net) :
    for k in range(N):
        for i in range(N):
            if i != k:
                for j in range(N):
                    if j != k and j != i:
                        net[i][j] = min(net[i][k]+net[k][j], net[i][j])



for tc in range(1,T+1):
    arr = list(map(int, input().split()))

    N= arr[0]
    # print(arr)

    net = []

    for i in range(1, len(arr), N):
        a = []
        for j in range(i, i+N):
            a += [arr[j]]
        net.append(a)
    # print(net)

    for i in range(len(net)):
        for j in range(len(net[i])):
            if net[i][j] == 0:
                net[i][j] = 100000000000


    # print(net)

    floyd(net)

    node = [0]*N

    for i in range(N):
        for j in range(N):
            if net[i][j] !=100000000000:
                node[i] += net[i][j]

    print('#{} {}' .format(tc, min(node)))