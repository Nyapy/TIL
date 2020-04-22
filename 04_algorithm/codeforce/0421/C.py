import sys

sys.stdin= open('C.txt')

T = int(input())

def AS(a,TF, count, hap):
    global result
    if count == n:
        result = hap+a
        return

    cur = seq[count]
    if cur >0 : nTF = True
    else : nTF= False
    if count :
        if TF == nTF:
            if a > cur:
                cur = a
        elif TF != nTF:
            hap += a

    AS(cur, nTF, count+1, hap)

for tc in range(T):
    n = int(input())
    seq = list(map(int, input().split()))
    result = 0
    AS(seq[0],True,0,0)
    print(result)