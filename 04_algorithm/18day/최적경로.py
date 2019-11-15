import sys
sys.stdin = open('최적경로.txt')

T = int(input())

def perm(n,k):
    if k == n :
        distance()

    else:
        for i in range(k,n):
            customer[k], customer[i] = customer[i], customer[k]
            perm(n, k+1)
            customer[i], customer[k] = customer[k], customer[i]

def distance():
    global shortest
    dist = 0
    # print(customer)
    for i in range(len(customer)-1):
        dist += abs(customer[i][0] - customer[i+1][0])+abs(customer[i][1] - customer[i+1][1])

    if shortest > dist :
        shortest = dist


for tc in range(1,T+1):
    N  = int(input())
    cus = list(map(int, input().split()))

    shortest = 200 * N

    customer = []
    A = [0]*len(customer)
    for i in range(0,len(cus),2):
        customer += [[cus[i], cus[i+1]]]

    # print(customer)
    customer.append(customer.pop(1))
    # print(customer)

    perm(N+1, 1)

    print('#{} {}' .format(tc, shortest))