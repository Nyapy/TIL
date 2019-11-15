'''
6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
->1
6
1 1 1 1 1 1
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
->0
6
10 20 10 20 30 40
0
0
0
0
0
0
-> -1
'''

# 게리 멘더링
#------------------

def DFS(v, group, visit):
    visit[v] = True
    ret = 1
    # 인접한 정점이 같은 그룹이고 방문 안 했으면
    for w in G[v]:
        if w in group and not visit[w]:
            ret += DFS(w, group, visit)
    return ret

def backtrack(k, A, B, sumA, sumB):
    if k == N + 1:
        global ans
        diff = abs(sumA - sumB)

        if len(B) == 0 or diff >= ans: return  # 0 이거나 정답보다 크면

        visit = [False] * (N + 1)   #visit 초기화
        if(DFS(A[0], A, visit) != len(A)): return

        visit = [False] * (N + 1)
        if(DFS(B[0], B, visit) != len(B)): return

        ans = diff
    else:   # 부분집합
        A.append(k)
        backtrack(k + 1, A, B, sumA + arr[k], sumB)
        A.pop()
        B.append(k)
        backtrack(k + 1, A, B, sumA, sumB + arr[k])
        B.pop()
#----------------------------------------------------

N = int(input())    # 2 ≤ N ≤ 10
arr = [0] + list(map(int, input().split())) # 인구수
G = [[0]]                                    # 인접 리스트, 0번 사용안함(빈값)

for i in range(N):
    tmp = list(map(int, input().split()))
    tmp.pop(0)      # 인접한 구역의 수
    G.append(tmp)

ans = 1000
A, B = [], []
A.append(1)   # 1이 A에 포함
backtrack(2, A, B, arr[1], 0)

if ans == 1000:
    ans = -1
print(ans)