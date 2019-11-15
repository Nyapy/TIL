import sys

sys.stdin = open('dessertcaffe.txt')

T = int(input())

def caffe(x,y):

    1


for tc in range(1,T+1):
    N = int(input())

    G = [list(map(int, input().split()))]

    for i in range(N-2):
        for j in range(1,N-1): #시작점 선택

            if j <= N - i - 1:
                a = j
            else:
                a = N - j - 1

            if N - i - 1 <= N - j:
                b = N - y - 1
            else:
                b = N - x

            for ld in range(1, a):
                for rd in range(1, b):