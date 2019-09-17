import sys
sys.stdin = open('(5186)이진수2_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    N = float(input())                          # float형으로 저장
    s = ""                                      # 빈 문자열 생성
    cnt = 0                                     # 자리수 기록
    print('#{}'.format(tc), end = ' ')
    while N != 0 and cnt < 13:                  # 0 이거나 13자리 이상이면 중단
        N *= 2
        cnt += 1
        if N >= 1:                              # 2를 곱해서 1이상이면 현재 자리수 1
            s += '1'
            N -= 1
        else:                                   # 2를 곱해서 1미만이면 현재 자리수 0
            s += '0'
    if cnt <= 12:
        print(s)
    else:
        print('overflow')
