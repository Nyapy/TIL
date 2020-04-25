from itertools import combinations

ips = ["5.5.5.5", "155.123.124.111", "10.16.125.0", "155.123.124.111", "5.5.5.5", "155.123.124.111", "10.16.125.0", "10.16.125.0"]
langs = ["Java", "C++", "Python3", "C#", "Java", "C", "Python3", "JavaScript"]
scores = [294, 197, 373, 45, 294, 62, 373, 373]

num = len(ips)

cheat = [0]*num
num_cheat = 0
for i in range(num):
    if langs[i] == "C++" or langs[i] =='C' or langs[i] =="C#":
        langs[i] = 0
    elif langs[i] == "Java":
        langs[i] = 1
    elif langs[i] == "JavaScript":
        langs[i] = 2
    else:
        langs[i] = 3

parti = dict()

for i in range(num):
    if cheat[i] == 1:
        pass
    else:
        tem = [i]
        ip = ips[i]

        for j in range(i+1, num):
            if cheat[i] == 1:
                pass
            if ips[j] == ip:
                tem.append(j)
        if tem :
            if len(tem) >= 4:
                for k in tem:
                    cheat[k] = 1
                num_cheat += len(tem)

            elif len(tem) == 3:
                if langs[tem[0]] == langs[tem[1]] == langs[tem[2]]:
                    for k in tem:
                        cheat[k] = 1
                    num_cheat += 3
                #
                # else:
                #     for i in combinations(tem, 2):
                #         if langs[i[0]] == langs[i[1]]:
                #             cheat[i[0]] = 1
                #             cheat[i[1]] =1
                #             num_cheat += 2

            if len(tem) ==2:
                if langs[tem[0]] == langs[tem[1]]:
                    if scores[tem[0]] ==scores[tem[1]]:
                        cheat[tem[0]] = 1
                        cheat[tem[1]] = 1
                        num_cheat += 2

print(num - num_cheat)
