import sys

sys.stdin = open("1713.txt")

tle = int(input())

rec_num = int(input())

recommend = list(map(int,input().split()))

students = [[0,0] for _ in range(101)]

picture = [0 for _ in range(tle)]

num=0

for i in range(rec_num):
    if num < tle:
        if recommend[i] in picture:
            students[recommend[i]][0] +=1
        else:
            students[recommend[i]][0] += 1
            students[recommend[i]][1] = i
            picture[num] = recommend[i]
            num += 1
    else:
        if recommend[i] in picture:
            students[recommend[i]][0] +=1

        else:
            tem = 1001
            temp = rec_num
            pic = tle
            pic_num = 0

            for j in range(tle):
                if students[picture[j]][0] < tem:
                    tem = students[picture[j]][0]
                    temp = students[picture[j]][1]
                    pic = j
                    pic_num = picture[j]
                elif  students[picture[j]][0] == tem:
                    if students[picture[j]][1] < temp:
                        tem = students[picture[j]][0]
                        temp = students[picture[j]][1]
                        pic = j
                        pic_num =picture[j]

            picture[pic] = recommend[i]

            students[recommend[i]][0] += 1
            students[recommend[i]][1] = i

            students[pic_num][0] = 0
            students[pic_num][1] = 0


picture.sort()
for i in range(tle):
    if picture[i] != 0:
        print(picture[i], end = " ")