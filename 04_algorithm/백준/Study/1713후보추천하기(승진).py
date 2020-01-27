import collections
import sys
sys.stdin = open("1713.txt")

N = int(input())
V = int(input())
S = list(map(int, input().split()))
voted = [0 for _ in range(101)]
ans = collections.deque()

for s in S:
    mini = 1001
    if s in ans:
        voted[s] += 1
    else:
        ans.append(s)
        voted[s] += 1

    if len(ans) > N:
        for an in range(len(ans)-1):
            if voted[ans[an]] < mini:
                mini = voted[ans[an]]
                a = ans[an]

        ans.remove(a)
        voted[a] = 0

for answer in sorted(ans):
    print(answer, end=" ")