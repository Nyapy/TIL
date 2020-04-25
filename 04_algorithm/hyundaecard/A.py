import sys

sys.stdin = open('A.txt')

purchase = []

for i in range(5):
    purchase.append(input())

br,si,go,pl,da = 0,0,0,0,0
grade =''
cur_price = 0

month = [0, 31, 28, 31, 30, 31, 30 , 31, 31,30,31, 30, 31]

cut = [10000,20000, 50000, 100000]

def bsg(price):
    global br, si, go, pl, da
    if price < cut[0]:
        br += 1
    elif price < cut[1]:
        si += 1
    elif price < cut[2]:
        go += 1
    elif price < cut[3]:
        pl += 1
    else :
        da += 1

year = [0]*366

for pur in purchase:
    i = pur.split(" ")
    date= i[0].split("/")
    price = int(i[1])

    mm = int(date[1])
    dd = int(date[2])
    tem = 0
    for i in range(mm):
        tem += month[i]
    tem += dd

    for i in range(tem, tem+30):
        year[i] += price

for j in range(1,366):
    bsg(year[j])

print(br, si, go, pl, da)




