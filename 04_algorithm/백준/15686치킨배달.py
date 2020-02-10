import sys

sys.stdin = open("15686.txt")

N,M = map(int, input().split())

cities = [0]+[[0]+list(map(int, input().split())) for _ in range(N)]

chicken = []
c_num = 0
house = []
h_num = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(1,N+1):
    for j in range(1,N+1):
        if cities[i][j] == 2:
            chicken.append([j,i])
            c_num +=1
        elif cities[i][j] == 1:
            house.append([j,i])
            h_num += 1

working = [0]*len(chicken)
result = 9876554321

def power(k, n):
    global result
    if M-k > c_num-n:
        return

    if k == M :

        chickendist = 0
        for i in range(h_num):
            tem = 99999921
            for j in range(c_num):
                if working[j] == 1:
                    dist = abs(chicken[j][0] - house[i][0]) + abs(chicken[j][1]-house[i][1])
                    if dist < tem:
                        tem = dist

            chickendist += tem

            # chickendist += bfs(x,y)

        if chickendist < result:
            result = chickendist

        return

    else:
        working[n] = 1
        power(k+1, n+1)
        working[n] = 0
        power(k, n+1)


power(0,0)

print(result)