import sys

sys.stdin = open('시간개념.txt')
T = int(input())

for tc in range(T):
    time1 = list(map(int, input().split(':')))
    time2 = list(map(int, input().split(':')))
    abs_sec = 3600*time1[0] + 

    print(time1, time2)