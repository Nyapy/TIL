import sys

sys.stdin = open('14888.txt')

N= int(input())

A = list(map(int, input().split()))

oper = list(map(int, input().split()))

max_ans = -1000000000
min_ans = 1000000000
def dfs(k,s):
    global max_ans, min_ans
    if k == N:
        if s > max_ans:
            max_ans = s
        if s < min_ans:
            min_ans = s
        return
    for i in range(4):
        if oper[i] >0:
            oper[i] -= 1
            if i == 0:
                dfs(k+1,s+A[k])
            elif i ==1:
                dfs(k + 1, s - A[k])
            elif i ==2:
                dfs(k + 1, s * A[k])
            elif i ==3:
                if s >= 0:
                    dfs(k + 1, s // A[k])
                elif s < 0:
                    dfs(k + 1, -1*(abs(s) // A[k]))

            oper[i] += 1

dfs(1,A[0])

print(max_ans)
print(min_ans)