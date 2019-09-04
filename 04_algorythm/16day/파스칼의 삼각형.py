import sys

sys.stdin = open('파스칼의 삼각형.txt')

T = int(input())

def pascal(n):
    if n == 1:
        tri = [1]
        return tri
    elif n == 0:
        tri = [1]
        return tri
    else :
        new_tri = []
        for i in range(n):
            if i == 0:
                new_tri += [1]
            elif i >= 0 and i < n-1:
                new_tri += [pascal(n-1)[i-1] + pascal(n-1)[i]]
            elif i == n-1:
                new_tri += [1]
        return new_tri

for tc in range(1,T+1):
    N = int(input())

    print('#{}' .format(tc))

    for i in range(1, N+1):
        a = pascal(i)
        for j in a:
            print(j, end = ' ')
        print()