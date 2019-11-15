import sys

sys.stdin = open('새로운 불면증 치료법.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    numbers = set()
    count = 1

    while len(numbers) < 10:
        A = N*count
        numbers.update(set(str(A)))
        count += 1

    count -= 1
    # print(numbers)
    print('#{} {}' .format(tc+1, count*N))