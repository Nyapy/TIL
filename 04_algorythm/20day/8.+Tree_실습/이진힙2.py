import sys
import heapq
sys.stdin = open("이진힙_input.txt", "r")
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    last = 0  # 노드가 하나도 없는 상태
    heap = []  # 이진 힙 구현을 위한 리스트 생성
    temp = list(map(int, input().split()))
    #
    for i in range(N):  # 힙에 저장
        heapq.heappush(heap, temp[i])
    # heapq.heapify(temp) # 리스트를 힙으로 변환

    for i in range(N):  # 힙에서 삭제
        print(heapq.heappop(heap), end=" ")
    print()

