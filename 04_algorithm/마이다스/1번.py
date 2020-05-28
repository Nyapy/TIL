strs = ["abcaefg", "abcdefg", "abcdhfg"]

# strs = ["a","b","c"]
min_length = min(map(len,strs))

pre = ""

for i in range(min_length):
    flag = 1
    tem = strs[0][i]
    for j in range(1,len(strs)):
        if strs[j][i] == tem:
            continue
        else:
            flag = 0
            break
    if flag:
        pre += tem
    else:
        break


print(pre)