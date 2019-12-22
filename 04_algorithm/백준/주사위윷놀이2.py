import sys

sys.stdin = open("주사위윷놀이.txt")

dice = list(map(int, input().split()))

area0 = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,41,41,41,41,41]
area1 = [0,2,4,6,8,10,13,16,19,25,30,35,40,41,41,41,41,41] #9 10 11 12
area2 = [0,2,4,6,8,10,12,14,16,18,20,22,24,25,30,35,40,41,41,41,41,41] # 13 14 15 16
area3 = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,28,27,26,25,30,35,40,41,41,41,41,41] #19 20 21 21

mal = [0 for _ in range(4)]
mal_area = [area0,area0,area0,area0]
max_score = 0

abcd = [0 for _ in range(10)]
abcd1 = [0 for _ in range(10)]
def is_there(k, area, num):
    for a in range(4):
        if a != k :
            if mal_area[a] == area  and mal[a] == num and mal_area[a][mal[a]] != 41:
                return False
            if area == area1 or area == area2 or area == area3:
                if mal_area[a] == area1 or area == area2 or area == area3:
                    if mal_area[a][mal[a]] == area[num]:
                        return False

    return True

def yoot(dice_num, score):
    global max_score
    if score == 193:
        azz = 123123
    if score + (10-dice_num)*40 < max_score:
        return
    cnt = 0
    if dice_num == 10:
        if max_score < score:
            max_score = score
        return

    for a in range(4):
        origin = mal[a]
        origin_area = mal_area[a]

        if mal_area[a][origin] == 41:
            cnt += 1
            continue

        tem_mal = mal[a] + dice[dice_num]

        if is_there(a, mal_area[a], tem_mal):
            mal[a] = tem_mal
            if origin_area == area0:
                if tem_mal == 5:
                    mal_area[a] = area1
                elif tem_mal == 10:
                    mal_area[a] = area2
                elif tem_mal == 15:
                    mal_area[a] = area3

            if mal_area[a][mal[a]] == 41:
                abcd[dice_num] = a
                yoot(dice_num + 1, score)
                mal[a] = origin
                mal_area[a] = origin_area
            else:
                abcd[dice_num] = a
                abcd1[dice_num] = mal_area[a][mal[a]]
                yoot(dice_num + 1, score + mal_area[a][mal[a]])
                mal[a] = origin
                mal_area[a] = origin_area

            if origin_area == area0 and origin == 0:
                break

    if cnt == 4:
        yoot(dice_num+1,score)

yoot(0,0)
print(max_score)