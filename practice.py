num = input()
a = list(range(0,10))
b=[0]*10
c=[]
c.extend(num)

for i in a:
   for j in c:
      if int(j) == i:
         b[i] += 1

for k in a:
   print('{} '.format(k), end='')
print()
for l in b:
   print('{} ' .format(l), end='')