import sys

sys.stdin = open('9084coin.txt')

T = int(input())

for tc in range(1,1+T):
    N = int(input())
    change = list(map(int, input().split()))

    bill = int(input())

    limit = bill//change[0]
    for i in range(limit):
