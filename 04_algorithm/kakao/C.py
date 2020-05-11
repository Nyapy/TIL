


import sys
sys.setrecursionlimit(10000)

cal_answer = []
def select_gem(k, arr, n, answer, pick):
    global cal_answer
    if k == n:
        pick.sort()
        res = pick + answer
        res.sort()
        if res[-1] - res[0] < cal_answer[-1] - cal_answer[0]:
            cal_answer = [res[0], res[-1]]
        elif res[-1] - res[0] == cal_answer[-1] - cal_answer[0]:
            if res[0] < cal_answer[0]:
                cal_answer = [res[0], res[-1]]
        return
    for gem in arr[k]:
        select_gem( k +1, arr, n, answer, pick+[gem])

def solution(gems):
    global cal_answer
    answer = []
    cal_answer = [0, len(gems)]


    lists = dict()

    for i in range(len(gems)):
        if lists.get(gems[i]):
            lists[gems[i]] += [i]
        else:
            lists[gems[i]] = [i]
    del_list = []
    selects = []
    for i in lists.keys():
        if len(lists[i]) == 1:
            del_list.append(i)
            if len(answer) < 2:
                answer.append(lists[i][0])
                answer.sort()
            else:
                if lists[i][0] < answer[0]:
                    answer[0] = lists[i][0]
                elif lists[i][0] > answer[1]:
                    answer[1] = lists[i][0]
        else:
            selects.append(lists[i])

    while selects:
        not_change = 1
        for i in range(len(selects)):
            if len(answer) > 1:
                if selects[i][-1] < answer[0]:
                    answer[0] = selects[i][-1]
                    del selects[i]
                    not_change = 0
                    break
                elif selects[i][0] > answer[1]:
                    answer[1] = selects[i][0]
                    del selects[i]
                    not_change = 0
                    break
                else:
                    flag = 0
                    for sel_in_num in selects[i]:
                        if answer[0] < sel_in_num < answer[1]:
                            del selects[i]
                            not_change = 0
                            flag = 1
                            break
                    if flag:
                        break
        if not_change:
            break
    select_gem(0, selects, len(selects), answer, [])
    answer = [cal_answer[0]+1, cal_answer[-1]+1]
    return answer