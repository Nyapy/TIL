land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]

height = 3
answer = 987654321

dx = [0,0,-1,1]
dy = [1,-1,0,0]

visited = [[0 for _ in range(N)] for _ in range(N)]

def dfs(x,y, visited, score,dep):


def solution(land, height):
    global answer
    N = len(land)


    for i in range(N):
        for j in range(N):
            dfs(j,i,visited,0,1)

    return answer