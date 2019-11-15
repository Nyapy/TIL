num = list(map(int, input().split()))
n3 = 0
n5 = 0
for a in num:
    if a % 3 == 0 :
        n3 += 1
    if a % 5 == 0 :
        n5 += 1

print("Multiples of 3 : {}".format(n3))
print("Multiples of 5 : {}".format(n5))