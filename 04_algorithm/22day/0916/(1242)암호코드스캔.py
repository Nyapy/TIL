import sys
sys.stdin = open("(1242)암호코드스캔_input.txt")

asc = [[0, 0, 0, 0],  #0
       [0, 0, 0, 1],  #1
       [0, 0, 1, 0],  #2
       [0, 0, 1, 1],  #3
       [0, 1, 0, 0],  #4
       [0, 1, 0, 1],  #5
       [0, 1, 1, 0],  #6
       [0, 1, 1, 1],  #7
       [1, 0, 0, 0],  #8
       [1, 0, 0, 1],  #9
       [1, 0, 1, 0],  #A
       [1, 0, 1, 1],  #B
       [1, 1, 0, 0],  #C
       [1, 1, 0, 1],  #D
       [1, 1, 1, 0],  #E
       [1, 1, 1, 1]]  #F

scode = [[[0 for _ in range(5)]for _ in range(5)]for _ in range(5)]
scode[2][1][1] = 0
scode[2][2][1] = 1
scode[1][2][2] = 2
scode[4][1][1] = 3
scode[1][3][2] = 4
scode[2][3][1] = 5
scode[1][1][4] = 6
scode[3][1][2] = 7
scode[2][1][3] = 8
scode[1][1][2] = 9

def solve():
    rst = 0
    for i in range(N):
        j = M * 4 - 1
        while j > 0:
            if arr[i][j] == 1 and arr[i - 1][j] == 0:
                code = [0 for _ in range(8)]
                for k in range(7, -1, -1):
                    x = y = z = 0
                    while arr[i][j] == 1:  # 1의 개수
                        z += 1
                        j -= 1
                    while arr[i][j] == 0:  # 0의 개수
                        y += 1
                        j -= 1
                    while arr[i][j] == 1:  # 1의 개수
                        x += 1
                        j -= 1
                    while arr[i][j] == 0:  # 0의 개수
                        j -= 1

                    d= min(x, y, z)
                    x //= d
                    y //= d
                    z //= d

                    code[k] = scode[x][y][z]

                t = (code[0] + code[2] + code[4] + code[6]) * 3 + code[1] + code[3] + code[5] + code[7]
                if t % 10 == 0:
                    rst += code[0] + code[2] + code[4] + code[6] + code[1] + code[3] + code[5] + code[7]
                j += 1   # 다음번 암호를 위해서
            j -= 1
    return rst

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr=[[0 for _ in range(M * 4)] for _ in range(N)]
    for i in range(N):
        temp = input()
        for j in range(M):
            t = temp[j]
            if t <= '9': t = ord(t) - ord('0')
            else : t = ord(t) - ord('A') + 10
            for k in range(4):
                arr[i][j*4+k] = asc[t][k]

    ans = solve()
    print("#{} {}".format(tc+1, ans))
