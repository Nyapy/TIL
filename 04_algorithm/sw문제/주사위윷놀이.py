dice = list(map(int, input().split()))

mal = [0,0,0,0]

pan = list(range(0,42,2))+[13,16,19]+[22,24]+[28,27,26]+[25,30,35,0]

result = 0

visited = [0 for _ in range(33)]

index = [ [i, i+1, i+2, i+3, i+4, i+5] for i in range(0,33) ]
index[5] = [5,21,22,23,29,30]
index[10] = [10,24,25,29,30,31]
index[15] = [15,26,27,28,29,30]
index[16] = [16,17,18,19,20,32]
index[17] = [17,18,19,20,32,32]
index[18] = [18,19,20,32,32,32]
index[19] = [19,20,32,32,32,32]
index[20] = [20,32,32,32,32,32]
index[21] = [21,22,23,29,30,31]
index[22] = [22,23,29,30,31,20]
index[23] = [23,29,30,31,20,32]
index[24] = [24,25,29,30,31,20]
index[25] = [25,29,30,31,20,32]
index[26] = [26,27,28,29,30,31]
index[27] = [27,28,29,30,31,20]
index[28] = [28,29,30,31,20,32]
index[29] = [29,30,31,20,32,32]
index[30] = [30,31,20,32,32,32]
index[31] = [31,20,32,32,32,32]
index[32] = [32,32,32,32,32,32]


def yute(dicenumber, score):
    global result
    if dicenumber == 10:
        if result < score:
            result = score
        return

    for a in range(4):
        origin = mal[a]
        tem = index[mal[a]][dice[dicenumber]]
        if visited[tem] == 1:
            continue
        else:
            mal[a] = tem

            visited[origin] = 0
            visited[tem] = 1

            visited[32] = 0

            yute(dicenumber+1, score+pan[mal[a]])
            mal[a] = origin

            visited[origin] = 1
            visited[tem] = 0
        if origin == 0:
            continue

yute(0,0)

print(result)