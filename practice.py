# c = []
#
# for a in range(1,201):
# 	if a%7 == 0 and a%5 !=0:
# 		c.append(str(a))
#
# ch = ','.join(c)
#
# print(ch)
num = 5
def A():
    global num
    print(num)
    num = 2
    print(num)
    B()

def B():
    global num
    print(num)
    num = 1
    print(num)

print(num)

A()

print(num)