import sys

sys.stdin = open("max-min_input.txt")
sys.stdout = open("max-min_output.txt", "w")
T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max = arr[0]
    min = arr[0]
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
    print("#{} {}" .format(tc+1, max-min))
