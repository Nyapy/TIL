import collections
import sys
sys.stdin = open("회전_input.txt","r")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    deq = collections.deque(data)

    for i in range(M): # M번 뒤로 보내기
        deq.append(deq.popleft())

    print("#{} {}".format(tc+1, deq.popleft()))