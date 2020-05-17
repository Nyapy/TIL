import sys

sys.setrecursionlimit(100001)

numbers = [3, 30, 34, 5, 9]

def perm(n,k,e,numbers):
    global answer
    tem = ""
    if e != 0:
        for j in range(k):
            tem += str(numbers[j])
        if int(tem) < int(answer[:e]):
            return

    if k == n :
        answer = tem

        return

    else:
        for i in range(k,n):
            numbers[i], numbers[k] = numbers[k], numbers[i]
            perm(n, k+1, e+len(str(numbers[k])), numbers)
            numbers[i], numbers[k] = numbers[k], numbers[i]

answer = ""

def solution(numbers):
    global answer
    for i in numbers:
        answer += str(i)

    perm(len(numbers),0,0,numbers)
    return answer

print(solution(numbers))