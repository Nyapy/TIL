import sys

sys.stdin=open("수영장.txt")

T = int(input())

def swim(k,S):
    global result
    if result <= S:
        return
    if k > 12:
        result = S

    else:
        swim(k+1,S+(price[0]*plan[k]))
        swim(k+1, S+price[1])
        swim(k+3,S+price[2])

for tc in range(1,T+1):
    price = list(map(int, input().split()))
    plan = [0]+list(map(int, input().split()))
    result = price[-1]
    swim(0,0)
    print("#{} {}" .format(tc,result))