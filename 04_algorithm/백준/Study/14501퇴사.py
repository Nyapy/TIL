import sys

sys.stdin= open("14501.txt")

N = int(input())

work =[list(map(int, input().split())) for _ in range(N)]

# print(work)

result = 0

def do(n,s):
    global result
    if n > N:
        return
    elif n == N:
        if result >= s:
            return
        else:
            result = s
            return

    do(n+1,s)
    do(n+work[n][0], s+work[n][1])

do(0,0)

print(result)