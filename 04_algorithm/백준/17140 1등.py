def transpose(board, row_num, col_num):
    temp = [[] * row_num for _ in range(col_num)]
    for i, line in enumerate(board):
        for j, ele in enumerate(line):
            temp[j].append(ele)

        for _ in range(col_num - len(line)):
            j += 1
            temp[j].append(0)

    return temp


i, j, k = map(int, input().split())
i -= 1
j -= 1

board = [list(map(int, input().split())) for _ in range(3)]

row_len = 3
col_len = 3

cnt = 0

trans_flag = False

flag = 1
if row_len > i and len(board[i]) > j and board[i][j] == k:
    flag = 0

while cnt <= 100 and flag == 1:
    if row_len < col_len or (trans_flag and row_len == col_len):
        board = transpose(board, row_len, col_len)

        i, j = j, i
        row_len, col_len = col_len, row_len

        trans_flag ^= True

    cnt += 1

    for r_num, row in enumerate(board):
        r_set = sorted(set(row))

        if r_set[0] == 0:
            r_set.remove(0)

        temp_list = []
        c_list = [row.count(ele) for ele in r_set]

        for r, c in zip(r_set, c_list):
            temp_list.append([r, c])

        temp_list.sort(key=lambda t: t[1])


        if len(temp_list) > 50:
            temp_list = temp_list[:50]

        new_list = []

        [new_list.extend(li) for li in temp_list]

        board[r_num] = new_list

        if col_len < len(new_list) or r_num == 0:
            col_len = len(new_list)

    flag = 1
    if row_len > i and len(board[i]) > j and board[i][j] == k:
        flag = 0

if cnt > 100:
    cnt = -1

print(cnt)