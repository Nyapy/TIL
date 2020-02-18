import sys

sys.stdin = open("13913.txt")
from collections import deque
def solve(visited,N,K):
    queue=deque()
    queue.append(N)
    while queue:
        t=queue.popleft()
        for num in (t+1,t-1,t*2):
            if 0<=num <=100000 and visited[num] == -1:
                visited[num] = t
                queue.append(num)
                if num == K :
                    return

N,K = map(int, input().split())
cnt = 0
visited = [-1]* 100001
solve(visited,N,K)


cnt = 0
tem = []
A= K
while A != N:
    cnt += 1
    tem.append(A)
    A = visited[A]
tem.append(N)


print(cnt)

for i in range(cnt,-1,-1):
    print(tem[i],end=" ")


