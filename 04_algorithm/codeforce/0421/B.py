import sys

sys.stdin= open('B.txt')

T = int(input())

for tc in range(1,1+T):
    n = int(input())
    half = n//2
    if half%2 :
        print('NO')

    else:
        print('YES')

        first = list(range(2,2*half+1,2))
        second = list(range(1,2*(half-1)+1,2))
        second.append(half*2+half-1)
        for i in first:
            print(i, end=" ")
        for i in second:
            print(i, end=" ")
        print()