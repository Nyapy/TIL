import sys

sys.stdin = open('16진수.txt')

hexa = list(input())

tem = []

for i in hexa:
    if '0' <= i <='9':
        tem.append(ord(i)-ord('0'))
    else:
        tem.append(ord(i)-ord('A')+10)
binary = []

for j in tem:
    a = int(j)
    imsi = []
    while a > 0 :
        b = a % 2
        a //= 2
        imsi.insert(0,b)
    while len(imsi) < 4:
        imsi.insert(0,0)
    binary += imsi

while len(binary) >= 7 :
    n = 0
    for k in range(7):
        n = n*2 + binary.pop(0)
    print(n)

n = 0
leng = len(binary)
for l in range(leng):
    n = n*2 + binary.pop(0)
print(n)