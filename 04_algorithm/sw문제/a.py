a, b = map(int, input().strip().split(' '))
time = [int(input()) for _ in range(a)]

con1 = 0
con2 = 0
curt = 0
i = 0

while i < len(time):
    if con1 == 0:
        con1 = time[i]
        i += 1
    if con2 == 0:
        if i == len(time):
            break
        con2 = time[i]
        i += 1
    if con1 > con2:
        curt += con2
        con1 -= con2
        con2 = 0

    elif con1 < con2:
        curt += con1
        con2 -= con1
        con1 = 0


    elif con1 == con2:
        con1, con2 = 0, 0
        curt += con1
if con1 == 0:
    curt += con2
elif con2 == 0:
    curt += con1
print(curt)