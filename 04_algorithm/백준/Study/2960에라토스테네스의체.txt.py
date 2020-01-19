import sys

sys.stdin = open("2960.txt")

N,K = map(int, input().split())

a= min(N+1,1001)
numbers = list(range(2,a))

visited = [0 for _ in range(2, a)]

cnt = 0

flag = 1
result = 0
while flag:
    for i in range(a-2):
        if visited[i] == 0:
            je = i
            break

    for j in range(je, a-2):
        if numbers[j]%numbers[je] == 0:
            if visited[j] == 0:
                visited[j] = 1
                cnt +=1
                if cnt == K:
                    flag = 0
                    result = numbers[j]
        if flag == 0:
            break
    if flag == 0:
        break

print(result)