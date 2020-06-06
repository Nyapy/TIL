import sys

sys.stdin = open("14889.txt")

from itertools import combinations as c
s=sum;u=input
n=int(u())
b=[[*map(int,u().split())]for _ in'a'*n]
d=[s(i)+s(j)for i, j in zip(b,zip(*b))]
S=s(d)//2
a=9**9
for l in c(d[:-1],n//2):
    a=min(a, abs(S-s(l)))
    if a==0:break
print(a)