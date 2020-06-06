import sys

sys.stdin = open("1525.txt")

from collections import deque

board = []
for i in range(3):
    tem = input().split()
    board += tem

visited = dict()
visited[str(board)] = 1
for i in range(len(board)):
    if board[i] =="0":
        zero = i

a = [[1,3],[0,4,2],[1,5],[0,4,6],[1,3,5,7],[2,4,8],[3,7],[4,6,8],[5,7]]

def listtostr(li):
    a = ''
    for i in li:
        a += i
    return a

def strtolist(st):
    l = []
    for i in st:
        l.append(i)
    return l

def nine(st):
    1

# print(ord("0"))
# print(ord("8"))

def bfs(zero):
    q = deque()
    visited = dict()
    te = listtostr(board)
    visited[te] = 0
    q.append(te)

    while q:
        mun = q.popleft()
        time = visited.get(mun)
        ze = mun.index('0')
        mun = strtolist(mun)
        for n in a[ze]:
            mun[ze],mun[n] = mun[n],mun[ze]
            tem = listtostr(mun)
            if not visited.get(tem):
                visited[tem] = time+1
                if tem == "123456780":
                    return time+1

                q.append(tem)
            mun[ze], mun[n] = mun[n], mun[ze]
    return -1

if listtostr(board)== '123456780':
    print(0)
else: print(bfs(zero))