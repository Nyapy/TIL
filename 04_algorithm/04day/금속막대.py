import sys

sys.stdin = open('금속막대_input.txt')

T = int(input())

for tc in range(T):
    N = int(input())

    a =list(map(int, input().split()))
    bolt = []
    count = 0
    ans = []
    c = 0

    for i in range(N):
        bolt.append([a[2*i], a[2*i+1]])
    # print(bolt)

    for i in range(N):
        if i == 0:
            ans.append(bolt[i])
            bolt[i] = [0,0]

        else:
            for j in bolt:
                if j[0] == ans[-1][1]:
                    ans.append(j)
                    j = [0, 0]

                elif j[1] == ans[0][0]:
                    ans.insert(0, j)
                    c +=1
                    j = [0, 0]

    print("#{}" .format(tc+1), end = ' ')
    for i in range(N):
        for j in range(2):
            print("{}" .format(ans[i][j]), end = ' ')
    print()