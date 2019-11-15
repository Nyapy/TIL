def calc():
    global minV
    food1 = 0  #음식1의 합
    food2 = 0  #음식2의 합
    visited = [0] * N

    #음식1의 재료 체크
    for i in range(N//2):
        visited[T1[i]] = 1

    #음식2의 조합(T2) 만들기
    idx = 0
    for i in range(N):
        if visited[i] == 0:
            T2[idx] = i
            idx += 1

    #각 음식의 합 구하기
    for i in range(N//2):
        for j in range(N//2):
            food1 += arr[T1[i]][T1[j]]
            food2 += arr[T2[i]][T2[j]]

    #차의 최소값 구하기
    if minV > abs(food1-food2):
        minV = abs(food1-food2)

def comb(n, r):
    if r == 0:
        calc()
    elif n < r:
        return
    else:
        T1[r-1] = A[n-1]
        comb(n-1, r-1)
        comb(n-1, r)

import sys
sys.stdin = open("(4012)요리사_input.txt")
T = int(input())
for tc in range(1, T+1):
    minV = 987654321
    N = int(input())  # 4 ≤ N ≤ 16, N:짝수
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = list(range(N))
    T1 = [0] * (N // 2) # 음식1의 조합
    T2 = [0] * (N // 2) # 음식2의 조합

    comb(N, N//2)
    print("#{} {}".format(tc, minV))