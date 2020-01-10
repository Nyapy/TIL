A = [[0] *7 for _ in range(3)]
B = [[0 for _ in range(7)] for _ in range(3)]
C = [[0 for _ in range(7)] * 3]
D = [[0 for _ in range(7)]] * 3

E = [[5,5],[2,2]]

def A(a):
    a[0] = 1

mal_on = [0, 3, 4, 3, 5, 1]

def reverse(x, k, rev, bef):
    rev[k] = x
    if mal_on[x] == x:
        mal_on[x] = bef
        return
    else:
        reverse(mal_on[x], k+1, rev, x)
    mal_on[x] = bef
rev = [3,1,5,4,2]


dist = list([[]])*10
dist2 = [[] for _ in range(10)]


dist[2] += [2]
dist2[2] += [2]
print(dist)
print(dist2)

M = 5
data = [[0] * (M) for _ in range(M)]

data[1][1] =1

print(data)

a = 15
for i in range(4):
    if a & (1 << i):
        print(i)