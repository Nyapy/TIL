import sys
sys.stdin = open("(2105)디저트카페_input.txt")
T = int(input())

#isVisit배열을 모두 False로 초기화
def visitClear():
    for i in range(101):
        visited[i] = 0

def solve():
    global result

    # i, j 좌표부터 시작
    for i in range(N):
        for j in range(N):
            # 사각형의 변의 길이는 각각  a(\), b(/)
            for a in range(1, N):  
                for b in range(1, N):
                    '''
                    result : 지금까지 계산한 값들 중에 가장 많이
                    디지트를 먹을 수 있는 결과 값을 저장하고 있다.
                    꼭지점이 존재할 수 있는지 범위를 확인하고,
                    지금 구할 둘레가 이전에 구했던 가장 큰 둘레보다
                    작으면 탐색하지 않는다.
                    '''

                    # 오른쪽, 아래, 왼쪽, 이전에 구했던 값보다 크다면
                    if(j + a <= N-1 and i + a + b <= N-1 and j - b >= 0 and (a+b)*2 > result) :
                        visitClear()
                        isAble = True
                        curi = i
                        curj = j

                        #우측하단(3시)
                        for n in range(a):
                            curi += 1
                            curj += 1
                            if not visited[MAP[curi][curj]]:
                                visited[MAP[curi][curj]] = 1
                            else:
                                isAble = False
                                break
                        if not isAble: continue

                        # 좌측 하단(6시)
                        for n in range(b):
                            curi += 1
                            curj -= 1
                            if not visited[MAP[curi][curj]]:
                                visited[MAP[curi][curj]] = 1
                            else:
                                isAble = False
                                break
                        if not isAble: continue

                      #좌측 상단(9시)
                        for n in range(a):
                            curi -= 1
                            curj -= 1
                            if not visited[MAP[curi][curj]]:
                                visited[MAP[curi][curj]] = 1
                            else:
                                isAble = False
                                break
                        if not isAble: continue

                     #우측 상단(12시)
                        for n in range(b):
                            curi -= 1
                            curj += 1
                            if not visited[MAP[curi][curj]]:
                                visited[MAP[curi][curj]] = 1
                            else:
                                isAble = False
                                break
                        if not isAble: continue

                        result = 2 * (a + b)

for tc in range(T):
    #맵 사이즈 저장한 변수
    N = int(input())
    #맵 정보를 저장한 배열
    MAP = [list(map(int, input().split())) for _ in range(N)]
    # 카페(번호) 방문 여부 체크용 배열
    visited = [0 for _ in range(101)]
    #가장 긴 경로길이 저장하는 변수
    result = -1

    solve()
    print("#{} {}".format(tc+1, result))

