def factorial(n):
    if n  == 1:
        return 1
    else :
        return factorial(n-1) * n

def fibo(n):
    if n < 2 :
        return n
    else :
        return fibo(n-1)+fibo(n-2)

print(factorial(3))
print(fibo(10))


def fib_memoization(n):
    global memo
    if n >=2 and len(memo) <= n :
        memo.append(fib_memoization(n-1)+ fib_memoization(n-2))
    return memo[n]

memo = [0, 1]

print(fib_memoization(9))
# 1000 넘으면 계산할 수 있는 범위를 넘어서 안됨