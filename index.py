import heapq

heap1 = [11,24,57,80]

heapq.heapify(heap1)
heapq.heappush(heap1,4)
heapq.heappush(heap1,10)
heapq.heappush(heap1,5)

minElement = heapq.heappop(heap1)
secondElement = heapq.heappop(heap1)
print(minElement)
print(secondElement)

print(heap1)

heap2 = [1,2,3,4,5]
heapq.heapify(heap2)
heapq.heappop(heap2)
print(heap2)