three = [0]
n = 9
num = 0
length = 0
while num < n:
    tem = 3**num
    tem_list = []
    for i in three:
        tem_list.append(tem+i)
        length += 1
        if length == n :
            break

    three = three + tem_list
    if length == n:
        break
    num+= 1

print(three[n])
