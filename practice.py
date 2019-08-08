c = []

for a in range(1,201):
	if a%7 == 0 and a%5 !=0:
		c.append(str(a))

ch = ','.join(c)

print(ch)
