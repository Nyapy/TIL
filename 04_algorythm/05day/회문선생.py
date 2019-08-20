def rowCount(arr):
    global flag, cnt, MAXSIZE
    for i in range(MAXSIZE):
        for j in range(MAXSIZE-N+1):
            flag = 1
            for k in range(N//2):
                if arr[i][j+k] != arr[i][j+N-1-k]:
                    flag = 0
            if flag : cnt += 1

def colCount(arr):
    global flag, cnt, MAXSIZE
    for i in range(MAXSIZE):
        for j in range(MAXSIZE-N+1):
            flag = 1
            for k in range(N//2):
                if arr[j+k][i] != arr[j+N-1-k][i]:
                    flag = 0
            if flag : cnt += 1
import sys
sys.stdin = open("회문_input.txt")
T = 10
MAXSIZE = 8
for tc in range(T):
    N = int(input())
    arr = [[0 for _ in range(MAXSIZE)]for _ in range(MAXSIZE)]
    for i in range(len(arr)):
        arr[i] = list(input())
    print(arr)
    flag = 0
    cnt = 0
    rowCount(arr)
    colCount(arr)
    print("#{} {}".format(tc+1, cnt))