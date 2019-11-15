# arr[0...n-1][0...n-1] : 2차원 list

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dx[i]
            print(arr[testX][testY])