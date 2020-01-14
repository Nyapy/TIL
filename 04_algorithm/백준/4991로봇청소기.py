import sys

sys.stdin = open("4991.txt")

flag = 1

while flag:
    w,h = map(int, input().split())
    if w == 0:
        break