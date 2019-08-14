


import sys
sys.stdin = open("prac1.txt")



def isWall(x,y):
    if x < 0 or y < 0 or x > 4 or y > 4 :
        return True
    return False

def calAbs(y,x):
    if y - x > 0:
        return y - x
    else :
        return x - y

arr = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    arr[i] = list(map(int, input().split()))

dx = [ 0, 0, -1, 1]
dy = [-1, 1, 0 , 0]

sum = 0

for x in range(len(arr)):
    for y in range(len(arr)):
        for i in range(4):
            TestX = x + dx[i]
            TestY = y + dy[i]
            if isWall(TestX, TestY) == False:
                sum += calAbs(arr[y][x], arr[TestY][TestX])

print("sum = {}" .format(sum))