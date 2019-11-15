import sys

sys.stdin = open('정곤이의 단조 증가하는 수.txt')

T = int(input())

def dangjo(N):
    rest = 9
    a = N
    while a != 0:
        b = a %10
        if b > rest:
            return
        rest = b
        a = a//10

    ans.append(N)

for tc in range(1,T +1):
    N = int(input())
    Num = list(map(int, input().split()))
    # print(Num)
    ans = [-1]
    can = []
    for i in range(N-1):
        for j in range(i+1,N):
            can.append(Num[i]*Num[j])

    for i in can:
        dangjo(i)

    # print(ans)



    print('#{} {}' .format(tc, max(ans)))