import sys
sys.stdin = open('c.txt')

N = int(input())
time = [list(map(int, input().split())) for i in range(N)]
cnt = 1
time.sort()
for i in range(len(time)):
    for j in range(i+1, len(time)):
        if time[i][1] > time[j][0]:
            cnt += 1

print(cnt)