import sys

sys.stdin = open('작업순서_input.txt')

T = 10


def work(v):

    cnt = 0
    for i in range(1,1+V):
        if path[i][v] != 0:
            cnt += 1
    if cnt == 0 and visited[v] == 0:
        print(v, end = ' ')
        visited[v] = 1
        for w in range(1,V+1):
             if path[v][w] == 1 :
                path[v][w] = 0
                work(w)



for tc in range(T):
    cnt = 0
    V, E = map(int, input().split())
    path_arr = list(map(int, input().split()))

    # print(path_arr)
    path = [[0 for i in range(V+1)] for j in range(V+1)]
    # print(path)

    visited = [0 for i in range(V+1)]

    for i in range(len(path_arr)//2):
        path[path_arr[2*i]][path_arr[2*i+1]] = 1

    # for i in range(len(path)):
    #     for j in range(len(path[i])):
    #         print(path[i][j], end = ' ')
    #     print()

    print('#{}' .format(tc+1), end = ' ')
    for j in range(1,V+1):
        work(j)
    print()

