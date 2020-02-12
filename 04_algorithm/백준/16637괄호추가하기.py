import sys

sys.stdin = open("16637.txt")

N = int(input())

susic = list(input())

numbers = []
express = []

for i in range(N):
    if (i % 2) == 0:
        numbers.append(int(susic[i]))
    else:
        express.append(susic[i])
# print(numbers)

A = [0]*(N//2)

result = -987654321

def power(k,n):
    global result
    if k == n :
        fir = numbers[0]
        s = 1
        i = 0

        while i < N//2:
            if A[i]:
                fir = calc(fir,numbers[s],express[i])
                s += 1
                i += 1
            else:
                if i == (N//2)-1 :
                    fir = calc(fir, numbers[s],express[i])
                    i+=1
                else:
                    if A[i+1]:
                        tem = calc(numbers[s],numbers[s+1],express[i+1])
                        fir = calc(fir,tem, express[i])
                        s += 2
                        i += 2

                    else:
                        fir = calc(fir, numbers[s], express[i])
                        s += 1
                        i += 1

        if fir > result:
            result = fir

    else:
        if 0 < k < n :
            if A[k-1] == 0:
                A[k] = 1
                power(k+1,n)
                A[k] = 0
                power(k+1, n)
            else:
                A[k] = 0
                power(k+1, n)
        elif k == 0:
            A[k] = 1
            power(k+1,n)
            A[k] = 0
            power(k+1,n)


def calc(a,b,c):
    if c == "+":
        return a+b
    elif c == "-":
        return a-b
    else:
        return a*b

power(0,N//2)

print(result)