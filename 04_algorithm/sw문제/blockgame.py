def solution(board):
    non = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                a = block(j,i,board[i][j])
    answer = 0
    return answer

def block(x, y, v):
    if board[y][x+2] == v :
        if board[y+1][x] == v :
            return -1
        elif board[y+1][x+2] == v:
            return -1
        elif board[y+1][x+1] == v:
            return -1

    elif board[y][x+1] == v:
        if board[y+2][x]:
            return -1
        elif board[y+2][x+1]:
            return -1

    elif board[y+2][x] ==v:
        if board[y+1][x+1] == v:
            return -1
        elif x-1 >= 0:
            if board[y+1][x-1] == v:
                return -1

    else:
        return 0