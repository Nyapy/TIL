import sys

sys.stdin = open('비트출력.txt')

bit = list(input())
binary = []


for i in range(0,len(bit),7):
    a= ''
    for j in range(7):
        a += bit[i+j]
    binary.append(a)

print(binary)

for i in binary:
    print(int(i, 2))