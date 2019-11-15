'''
3 4
0 1 0 0
0 0 0 0
0 0 1 0
'''

# 예시1
n, m = map(int, input().split())
mylist = [0 for _ in range(n)]
# mylist = [0] * n
for i in range(n) :
    mylist[i] = list(map(int, input().split()))
print(mylist)

#예시2
n, m = map(int, input().split())
mylist = []
for i in range(n):
    mylist.append(list(map(int, input().split())))
print(mylist)

#예시3
n, m = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(n)]
print(mylist)