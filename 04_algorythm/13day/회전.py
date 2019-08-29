import sys
sys.stdin = open('회전.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))

    for _ in range(M):
        first = seq.pop(0)
        seq.append(first)


    print('#{} {}' .format(tc, seq[0]))