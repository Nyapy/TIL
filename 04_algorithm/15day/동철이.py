import sys

sys.stdin = open('동철이.txt')

T = int(input())

for tc in range(T):
    N = int(input())

    poten = [list(map(int, input().split())) for _ in range(N)]

    print(poten)