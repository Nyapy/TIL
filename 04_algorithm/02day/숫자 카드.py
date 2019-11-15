import sys
sys.stdin = open("숫자 카드_input.txt")
sys.stdout = open("숫자 카드_output.txt", 'w')

T = int(input())

for tc in range(T):
    N = int(input())
    card = input()
    card_list = []
    card_count = [0]*10
    for i in card :
        a = int(i)
        card_count[a] += 1

    a = -1
    for j in range(10):
        if a <= card_count[j] :
            a = card_count[j]
            b = j
    print("#{} {} {}" .format(tc+1, b, a))




