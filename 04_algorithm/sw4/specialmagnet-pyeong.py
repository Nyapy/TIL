import sys

sys.stdin = open('specialmagnet.txt')

T = int(input())
for tc in range(1, T+1):
   K = int(input())
   m = [0]+[list(map(int, input().split())) for _ in range(4)]
   dj = [0] * 5
   bb = [0] * 5
   dn = [-1, 1]
   pd = [6, 2]
   nd = [2, 6]
   # for i in range(K):
   #     n, d = map(int, input().split())
   #     for j in range(2):
   #         tn = n + dn[j]
   #         if 1 <= tn < 5:
   #             if m[n-1][(dj[n] + pd[j]) % 8] ^ m[tn-1][(dj[tn] + nd[j]) % 8]:
   #                 b = -1
   #                 bb[tn] -= d * b
   #                 pn = tn
   #                 tn = tn + dn[j]
   #                 while 0 <= tn < 5 and 0 <= pn < 4 and m[pn-1][(dj[pn] + pd[j]) % 8] ^ m[tn-1][(dj[tn] + nd[j]) % 8]:
   #                     b *= -1
   #                     bb[tn] -= d * b
   #                     pn = tn
   #                     tn = tn + dn[j]
   #     dj[n] -= d
   #     for i in range(1,5):
   #         dj[i] += bb[i]
   #         bb[i] = 0
   #         if dj[i] < 0:
   #             dj[i] += 8
   # ret = 0
   # for i in range(1, 5):
   #     ret += m[i-1][dj[i] % 8] * 2 ** (i-1)
   # print("#{} {}" .format(tc, ret))
   #
   print(m)