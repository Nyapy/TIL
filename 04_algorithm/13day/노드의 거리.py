import sys

sys.stdin = open('노드의 거리.txt')

T = int(input())

def BFS(S):

    visited[S] = 1
    queue.append(S)

    while queue:
        t = queue.pop(0)
        for i in range(len(road[t])):
            if visited[i] == 0 and road[t][i] ==1:
                queue.append(i)
                visited[i] = visited[t]+1


for tc in range(T):

    V, E = map(int, input().split())
    line = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    road = [[0 for _ in range(V+1)] for __ in range(V+1)]
    visited = [0] *(V+1)
    queue = []

    for l in line:
        road[l[0]][l[1]] = 1
        road[l[1]][l[0]] = 1

    BFS(S)

    if visited[G] !=0:
        print('#{} {}' .format(tc+1, visited[G]-1))
    else :
        print('#{} {}' .format(tc+1, visited[G]))