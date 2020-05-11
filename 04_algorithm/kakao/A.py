numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = "right"
hand = "left"
def button(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]

    leri = [2,5,8,0]

    dist = [[1,2,3,4],[2,1,2,3],[3,2,1,2],[4,3,2,1],[0,1,2,3],[1,0,1,2],[2,1,0,1],[3,2,1,0]]
    #1,4,7,* 별 거리
    lthumb = 3
    rthumb = 3
    for i in numbers:
        if i in left:
            lthumb=left.index(i)
            answer +='L'

        elif i in right:
            rthumb=right.index(i)
            answer += 'R'

        else:
            num = leri.index(i)
            ldis = dist[lthumb][num]
            rdis = dist[rthumb][num]

            if ldis > rdis :
                answer += "R"
                rthumb = num+4
            elif rdis > ldis :
                answer += "L"
                lthumb = num+4
            else:
                if hand == "right":
                    answer += "R"
                    rthumb = num+4
                else :
                    answer += "L"
                    lthumb = num+4

    print(answer)

button(numbers, hand)