import sys
sys.stdin = open('p1.txt')

T = int(input())

for tc in range(1,1+T):
    N = int(input())

    road = [list(map(int, input().split())) for _ in range(N)]

    numbers = [0]*6

    row = N*5
    r_height = 5

    for i in range(N):
        for j in range(N):
            tem_sum = 0
            av = 0
            for k in range(N):
                numbers[road[i][k]] += 1
                numbers[road[k][j]] += 1
            numbers[road[i][j]] -= 1
            a = max(numbers)
            av = numbers.index(a)

            money = 0
            for k in range(N):
                money += abs(road[i][k] -av) + abs(road[k][j]-av)

            money -= abs(road[i][j]-av)

            if money < row :
                row = money
                if av < r_height:
                    r_height = av

    print('#{} {} {}' .format(tc, row, r_height))