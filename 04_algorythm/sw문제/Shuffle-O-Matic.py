import sys

sys.stdin = open('Shuffle-O-Matic.txt')

def shuffle(temp, x):
    global cola, count
    cnt = 0
    for i in range(x):
        if i < N//2:
            slice = c_n[N//2-i:N//2+i+1:2]
        if i >= N//2:
            slice = c_n[cnt:N//2+i+1:2]
            cnt +=1
        for j in slice:
            temp[j-1], temp[j] = temp[j], temp[j-1]
        # print(temp)
    if temp == ascend or temp == descent:
        cola = 1
    if x != 0:
        count += 1

def shuffleomatic(card):
    global cola, count
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    for e in range(N):
                        count = 0
                        tem =[a,b,c,d,e]
                        temp = card[:]
                        for i in tem:
                            shuffle(temp, i)
                            if cola == 1:
                                # print(tem)
                                return

    count = -1


T = int(input())

for tc in range(T):
    N = int(input())
    x = range(N)
    card = list(map(int, input().split()))
    c_n = []

    tem = []
    cola = -1
    for i in range(N):
        c_n += [i]

    # print(card)

    ascend = sorted(card)
    descent = sorted(card, reverse = True)
    count = 0

    shuffleomatic(card)

    if count <= 5:
        cola = count
    else:
        cola = -1

    print('#{} {}' .format(tc+1, cola))



