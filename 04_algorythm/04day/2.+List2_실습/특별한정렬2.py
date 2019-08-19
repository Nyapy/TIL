import sys

sys.stdin = open('특별한정렬_input.txt', 'r') # 파일에서 읽을 때 사용
T = int(input())
for tc in range (1, T+1):
    N = int(input())
    v = list(map(int, input().split()))
    w = v.copy()                    # 리스트 복사
    v.sort(reverse = True)          # 내림차순 정렬
    w.sort()                        # 오름차순 정렬

    print("#%d" % tc , end=' ')
    for j in range (0, 5):
        print(v[j], end=' ')
        print(w[j], end=' ')
    print()