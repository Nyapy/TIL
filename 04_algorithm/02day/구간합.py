import sys

sys.stdin = open("구간합_input.txt")
sys.stdout = open("구간합_output.txt", 'w')

T = int(input())

for tc in range(T):
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]
    integers = list(map(int, input().split()))


    for i in range(0, len(integers)-M +1):
        a_max = 0
        a_min = 0
        if i == 0:
            for j in range(i , i+M):
                a_max += integers[j]
                a_min += integers[j]
                sum_max = a_max
                sum_min = a_max
        a_max = 0
        a_min = 0
        for k in range(i, i+M):
            a_max += integers[k]
            a_min += integers[k]

        if sum_max < a_max:
            sum_max = a_max
        if sum_min > a_min:
            sum_min = a_min
    print("#{} {}".format(tc+1, sum_max-sum_min))
