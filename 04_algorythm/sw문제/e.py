import sys
sys.stdin = open('e.txt')

paper = list(map(int, input().split()))

cony = list(map(int, input().split()))

visited = [[0 for _ in range(paper[0]+ 1)] for __ in range(paper[1]+1)]
q = []

dx = [0,1]
dy = [1,0]

def hideseek():
    if cony[0] < 0 or cony[1] < 0 or cony[0] > paper[0] or cony[1] > paper[1]:
        print('fail')
        return

    else:
        bfs(0, 0)


def bfs(x, y):
    visited[y][x] = 1
    q.append([x, y])

    while q :
        t = q.pop(0)
        for k in range(2):
            nx = t[0] + dx[k]
            ny = t[1] + dy[k]
            if nx >= 0 and ny >= 0 and nx < paper[0]+1 and ny < paper[1]+1:
                if visited[ny][nx] == 0:
                    q.append([nx, ny])
                    if nx == 0:
                         visited[ny][nx] = visited[ny-1][nx]

                    elif ny == 0 :
                        visited[ny][nx] = visited[ny][nx-1]

                    else:
                        visited[ny][nx] = visited[ny][nx-1] + visited[ny-1][nx]

    print(cony[0]+ cony[1])
    print(visited[cony[0]][cony[1]])

hideseek()