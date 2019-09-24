T = int(input())


def calcu(N):
    l,r = 0, -1
    if 1 <= N <=1000000:
        if visited[N] == 0:
            visited[N] = 1
            nt = [N+1, N-1, N*2, N-10]

            for k in range(4):
                if 1<= nt[k] <= 1000000:
                    if visited[nt[k]] == 0:
                        visited[nt[k]] = visited[N] +1
                        q.append(nt[k])
                        r += 1
                    if nt[k] == M:
                        return

    while q:
        t= q[l]
        l += 1
        if 1 <= t <=1000000:
            nt = [t+1, t-1, t*2, t-10]

            for k in range(4):
                if 1<= nt[k] <= 1000000:
                    if visited[nt[k]] == 0:
                        visited[nt[k]] = visited[t] +1
                        q.append(nt[k])
                        r+= 1
                    if nt[k] == M:
                        return


for tc in range(1,T+1):
    N,M = map(int, input().split())
    visited = [0]*1000001

    q = []
    calcu(N)

    print('#{} {}' .format(tc, visited[M]-1))