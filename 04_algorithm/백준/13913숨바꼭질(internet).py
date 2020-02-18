import sys

sys.stdin = open("13913.txt")
from collections import deque
def solve(visited,n,k):
    queue=deque()
    queue.append(n)
    while queue:
        x=queue.popleft()

        if x==k:
            print(visited[x])
            p=[]
            while x!=n:
                p.append(x)
                x=path[x]
            p.append(n)
            p.reverse()
            print(' '.join(map(str,p)))
            return

        for nx in (x+1,x-1,x*2):
            if 0<=nx<100001 and visited[nx]==0:
                visited[nx]=visited[x]+1
                path[nx]=x
                queue.append(nx)

n,k=map(int,input().split())
visited=[0]*100001
path=[0]*100001
solve(visited,n,k)