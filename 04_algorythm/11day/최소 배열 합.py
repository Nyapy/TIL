T = int(input())

def com_sum(n):
    global ps, min_sum
    all = []
    ps = 0
    for i in range(n):
        all += [tem[i]]
    for a in range(len(all)):
        if ps > min_sum:
            return
        for b in range(len(all)):
            if all[a][b]:
                ps += arr[a][b]
                if ps > min_sum:
                    return
    if min_sum > ps:
        min_sum = ps

def perm(n, k):
    if k == n:
        com_sum(n)
    else:
        for i in range(k, n):
            tem[k], tem[i] = tem[i], tem[k]
            perm(n, k+1)
            tem[k], tem[i] = tem[i], tem[k]

for tc in range(T):
    N = int(input())
    tem = []
    all = []
    min_sum = 10*N

    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    count = 0
    while count < N :
        a = N-count-1
        tem += [[0]*count+[1]+[0]*a]
        count +=1

    # print(tem)
    perm(N, 0)
    print('#{} {}' .format(tc+1, min_sum))