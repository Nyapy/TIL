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

reverse(rev[-1],0, rev,rev[-1])
print(mal_on)
print(rev)