import sys
sys.stdin = open("view_input.txt")
sys.stdout = open("view_output.txt", 'w')
T = 10

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    resident = 0

    for i in range(2, len(arr)-2):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i-2] and arr[i] > arr[i+2]:
            a = arr[i-2]
            for j in [i-2, i-1, i+1, i+2] :
                if arr[j] > a:
                    a = arr[j]

            resident += arr[i] - a

    print("#{} {}" .format(tc+1, resident))
