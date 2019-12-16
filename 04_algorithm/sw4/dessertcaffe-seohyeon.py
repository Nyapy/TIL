def tour(x, y):
    dessert = [0] * 101
    dessert[m[y - 1][x - 1]] = 1
    d = 0
    ret = 1
    while [x, y] != corner[3]:
        if dessert[m[y][x]]:
            return -1
        if [x, y] == corner[d]:
            d += 1
        ret += 1
        dessert[m[y][x]] = 1
        x, y = x + dx[d], y + dy[d]
    return ret


for test_case in range(1, int(input()) + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, -1, -1, 1]
    dy = [1, 1, -1, -1]

    result = -1
    for i in range(0, N - 2):
        for j in range(1, N - 1):
            for k in range(N - j - 1, 0, -1):
                for l in range(j, 0, -1):
                    if i + k + l < N and result < (k + l) * 2:
                        corner = [[j + k, i + k], [j + k - l, i + k + l], [j - l, i + l], [j, i]]
                        ret = tour(j + 1, i + 1)
                        result = result if result > ret else ret

    print('#{} {}'.format(test_case, result))