def calc(value, i, op):
    if op == 0 : return value + nums[i]
    elif op == 1 : return value - nums[i]
    elif op == 2 : return value * nums[i]
    elif op == 3 : return int(value / nums[i])  # //로 하면 안됨

    return 0

def dfs(k, rst):
    global maxV, minV
    if k == N-1:
        maxV = max(rst, maxV)
        minV = min(rst, minV)
        return

    for i in range(4):
        if oper[i] == 0: continue
        oper[i] -= 1
        dfs(k + 1, calc(rst, k+1, i))
        oper[i] += 1

import sys
sys.stdin = open("(4008)숫자만들기_input.txt")
T = int(input())
for tc in range(1, T+1):
    maxV = -987654321
    minV = 987654321
    N = int(input())    # 숫자개수
    oper= list(map(int, input().split()))  # 연산자
    nums = list(map(int, input().split())) # 숫자

    dfs(0, nums[0])
    print("#%d" % tc, maxV - minV)


