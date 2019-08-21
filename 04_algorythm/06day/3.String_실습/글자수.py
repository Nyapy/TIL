import sys

sys.stdin = open("글자수_input.txt")  # 파일에서 입력받는 경우 사용
T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    asc = [0] * 128
    alph = []
    max = 0

    for i in range(len(str1)):  #중복제거
        asc[ord(str1[i])] += 1

    for i in range(len(asc)):
        if asc[i] :
           alph.append(chr(i))

    asc = [0] * 128             #count
    for i in range(len(str2)):
        for j in range(len(alph)):
            if str2[i] == alph[j] :
                asc[ord(str2[i])] += 1

    for i in range(len(asc)):  #최대값
        if max < asc[i] :
            max = asc[i]

    print("#{} {}".format(tc, max))

