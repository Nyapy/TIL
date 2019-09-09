import heapq

heap = [7, 2, 5, 3, 4, 6]
heapq.heapify(heap)
print(heap)
heapq.heappush(heap, 1)
print(heap)
while heap:
    print(heapq.heappop(heap), end = ' ')