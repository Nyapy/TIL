import sys

sys.stdin = open('베이비진.txt')

T = int(input())
def babygin(p):
    for i in range(0,len(p)-3+1):
            if p[i] == p[i+1] and p[i+1] == p[i+2]:
                return 1
            elif p[i]+1 == p[i+1] and p[i+1]+1 == p[i+2]:
                return 1
    return 0

def perm(n,k,arr):
    global flag
    if flag:
        return
    if n == k:
        flag = babygin(arr)
        return flag
    for i in range(k,n):
        arr[i], arr[k] = arr[k], arr[i]
        perm(n, k+1, arr)
        arr[i], arr[k] = arr[k], arr[i]

for tc in range(1,T+1):

    card = list(map(int, input().split()))
    p1 = []
    p2 = []
    a,b = 0,0

    for i in range(0,len(card),2):
        p1.append(card[i])
        p2.append(card[i+1])
        p1.sort()
        p2.sort()
        if len(p1) >= 3:
            flag = 0
            perm(len(p1), 0, p1)
            a = flag
            if a == 1 and b == 0:
                print("#{} 1" .format(tc))
                break
            elif a == 0 and b == 1:
                print("#{} 2" .format(tc))
                break
            elif a == 1 and b == 1:
                print("#{} 0" .format(tc))
                break

            flag = 0
            perm(len(p2), 0, p2)
            b = flag
            if a == 1 and b == 0:
                print("#{} 1" .format(tc))
                break
            elif a == 0 and b == 1:
                print("#{} 2" .format(tc))
                break
            elif a == 1 and b == 1:
                print("#{} 0" .format(tc))
                break


    if a == 0 and b == 0:
        print("#{} 0".format(tc))