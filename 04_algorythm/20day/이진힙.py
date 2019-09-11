import sys

sys.stdin = open('이진힙.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    tem = [0]
    ss= 0

    for i in nums:
        tem.append(i)
        if len(tem) >= 3:
            c = tem.index(tem[-1])
            p = c//2
            while p >= 1 :
                if tem[p] > tem[c] :
                    tem[p] , tem[c]  = tem[c], tem[p]
                    c = p
                    p = c//2
                else:
                    break
    a = len(tem)-1
    # print(tem)

    while a >= 1:
        ss += tem[a//2]
        a //= 2
    print('#{} {}' .format(tc, ss))


