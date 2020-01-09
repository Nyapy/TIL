import sys

sys.stdin = open("2309.txt")

nine = [int(input()) for _ in range(9)]

flag = 0
A= []
def seven(n, k, s, small):
    global flag
    if 7 - k > 9 - n:
        if k == 7:
            return

    if flag == 1:
        return
    if s >100:
        return

    if k == 7:
        if s == 100:
            small.sort()
            for i in range(7):
                print(small[i])
            flag = 1

    else:

        seven(n+1,k+1, s+nine[n], small+[nine[n]])
        seven(n+1,k,s, small)


seven(0,0,0,[])