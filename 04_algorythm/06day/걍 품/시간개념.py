import sys

sys.stdin = open('시간개념.txt')
T = int(input())

for tc in range(T):
    time1 = list(map(int, input().split(':')))
    time2 = list(map(int, input().split(':')))
    abs_sec1 = 3600*time1[0] + 60*time1[1] + time1[2]
    abs_sec2 = 3600 * time2[0] + 60 * time2[1] + time2[2]

    if abs_sec1 < abs_sec2:

        time_lag = abs_sec2 - abs_sec1

        hour = time_lag//3600
        minute = (time_lag%3600)//60
        sec = (time_lag % 3600) % 60

        time = []
        time += [hour]
        time += [minute]
        time += [sec]

    else:
        time_lag = (3600 * 24) - abs_sec1 + abs_sec2
        hour = time_lag // 3600
        minute = (time_lag % 3600) // 60
        sec = (time_lag % 3600) % 60

        time = []
        time += [hour]
        time += [minute]
        time += [sec]

    print("{:02}:{:02}:{:02}" .format(hour, minute, sec))

