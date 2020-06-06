import sys

sys.stdin = open('14888.txt')

def next_permutation(A):
    N = len(A)

    # 7 2 3 6 5 4 1
    i = N - 1
    # 1.
    while i > 0 and A[i-1] >= A[i]:
        i -= 1
    if i == 0:
        return False
    # 2.
    j = N - 1
    while j >= i and A[j] <= A[i-1]:
        j -= 1
    # 3.
    A[i-1], A[j] = A[j], A[i-1]
    # 4.
    j = N - 1
    while j > i:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1

    return True

def div(a, b):
    if a >= 0:
        return a // b
    else:
        return -(-a // b)


if __name__ == "__main__":

    n = int(input())
    nums = list(map(int, input().split()))
    # [+, -, *, /]
    n_ops = list(map(int, input().split()))

    ops = [0]*(n_ops[0]) + [1]*(n_ops[1]) + [2]*(n_ops[2]) + [3]*(n_ops[3])

    vals = []

    while True:
        val = nums[0]
        # 숫자 개수 = 연산자 개수 + 1
        for i in range(n-1):
            if ops[i] == 0:
                val += nums[i+1]
            elif ops[i] == 1:
                val -= nums[i+1]
            elif ops[i] == 2:
                val *= nums[i+1]
            else:
                val = div(val, nums[i+1])
        vals.append(val)

        if not next_permutation(ops):
            break

    print(max(vals))
    print(min(vals))