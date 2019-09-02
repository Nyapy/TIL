import sys
sys.stdin = open("(1486)장훈이의높은선반_input.txt")

def calc(n, k, cursum):
    global ans
    if cursum >= B:
        if ans > cursum:
            ans = cursum
        return

def powerset(n, k, cursum):
    if ans < cursum: return    # 가지치기

    if n == k:
        calc(n, k, cursum)
    else:
        A[k] = 1
        powerset(n, k + 1, cursum + h[k])
        A[k] = 0
        powerset(n, k + 1, cursum)

T = int(input())
for tc in range(T):
    N, B = map(int, input().split())        # 점원수, 선반
    h = list(map(int, input().split()))     # 점원의 키들
    A = [0] * N                             # h가 있으므로 사용 안 함
    ans = 0xfffffff
    powerset(N, 0, 0)

    print("#%d %d" % (tc+1, ans - B))
