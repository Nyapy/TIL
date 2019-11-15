import sys
sys.stdin = open("(2805)농작물 수확하기_input.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    # data = [[0 for _ in range(N)] for _ in range(N)]
    # for i in range(N): # 맨 앞에 0을 처리하기 위해 문자열로 받아서 숫자로 바꿈
    #     temp = input()
    #     for j in range(N):
    #         data[i][j] = int(temp[j])

    mid =  N // 2
    start = mid
    end = mid
    sum = 0
    for i in range(N):
        for j in range(start, end+1, 1):
            sum += data[i][j]
        if i < mid :
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print("#{} {}".format(tc, sum))

