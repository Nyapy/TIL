import sys

sys.stdin= open('17140.txt')

r,c,k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(3)]
R,C = 3,3
turn = 0

def Rcal():
    global R,C
    lenC =0
    NA = []
    for i in range(R):
        cnt = [0 for _ in range(101)]
        for j in range(C):
            if A[i][j]:
                cnt[A[i][j]] += 1

        nums = dict()
        for k in range(101):
            if cnt[k]:
                nums[k] = cnt[k]
        tem_R = []
        visited = [0 for _ in range(101)]
        for l in range(len(nums)):
            tn = 101
            tc = 999999
            for num, c in nums.items():
                if visited[num] == 0:
                    if tc > c:
                        tc = c
                        tn = num

                    if tc == c:
                        if tn > num:
                            tn = num
            tem_R.append(tn)
            tem_R.append(tc)
            visited[tn] =1

        NA.append(tem_R)
        if len(tem_R) > lenC :
            lenC = len(tem_R)
    C = lenC
    for a in NA:
        lena = len(a)
        for b in range(C-lena):
            a.append(0)

    return NA




def Ccal():
    global R,C
    lenR =0
    NA = []
    for i in range(C):
        cnt = [0 for _ in range(101)]
        for j in range(R):
            if A[j][i]:
                cnt[A[j][i]] += 1

        nums = dict()
        for k in range(101):
            if cnt[k]:
                nums[k] = cnt[k]
        tem_C = []
        visited = [0 for _ in range(101)]
        for l in range(len(nums)):
            tn = 101
            tc = 999999
            for num, c in nums.items():
                if visited[num] == 0:
                    if tc > c:
                        tc = c
                        tn = num

                    if tc == c:
                        if tn > num:
                            tn = num
            tem_C.append(tn)
            tem_C.append(tc)
            visited[tn] =1

        NA.append(tem_C)
        if len(tem_C) > lenR :
            lenR = len(tem_C)
    R = lenR
    for a in NA:
        lena = len(a)
        for b in range(R-lena):
            a.append(0)
    tem_NA = [[0 for _ in range(len(NA))] for _ in range(len(NA[0]))]
    for i in range(R):
        for j in range(C):
            tem_NA[i][j] = NA[j][i]

    return tem_NA


while turn <= 100:

    if R > r-1 and C > c-1:
        if A[r-1][c-1] == k:
            break
    if R >= C:
        A = Rcal()
    else:
        A = Ccal()
    turn += 1

if turn <= 100:
    print(turn)

else:
    print(-1)