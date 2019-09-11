# 최소힙만 지원
import heapq
heap = [7, 2, 5, 3, 4, 6]
heapq.heapify(heap)  #한번에 힙으로 변환
print(heap)
heapq.heappush(heap, 1)
print(heap)
while heap:
    print(heapq.heappop(heap), end = " ")
##########################
temp = [7, 2, 5, 3, 4, 6]
heap2=[]
for i in range(len(temp)):
    heapq.heappush(heap2, (-temp[i], temp[i])) #(우선순위, 값)
heapq.heappush(heap2, (-1, 1))
print(heap2)
while heap2:
    print(heapq.heappop(heap2)[1], end = " ")