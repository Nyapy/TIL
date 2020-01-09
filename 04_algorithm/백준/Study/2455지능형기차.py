import sys

sys.stdin = open("2455.txt")

person = 0
result = 0
for m in range(4):
    passen = list(map(int, input().split()))

    person += passen[1]
    person -= passen[0]
    if person > result :
        result = person


print(result)