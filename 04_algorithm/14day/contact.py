import sys

sys.stdin = open('contact.txt')

T = 10

def cal(v):
    Q= []
    Q.append(v)
    people[v] = 1

    while Q :
        t = Q.pop(0)

        for i in range(101):
            if contact[t][i]==1 and people[i] == 0 :
                Q.append(i)
                people[i] = 1+people[t]

for tc in range(1,T+1):
    data_len, start = map(int, input().split())
    data = list(map(int, input().split()))

    people = [0]*101

    contact = [[0 for _ in range(101)] for __ in range(101)]

    for i in range(0, data_len, 2):
        contact[data[i]][data[i+1]] = 1

    cal(start)
    a = max(people)
    for i in range(len(people)):
        if people[i] == a :
            b = i

    print('#{} {}' .format(tc, b))
