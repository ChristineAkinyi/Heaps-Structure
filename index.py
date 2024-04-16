import heapq

heap1 = [11,24,57,80]

heapq.heapify(heap1)
heapq.heappush(heap1,4)
heapq.heappush(heap1,10)
heapq.heappush(heap1,5)

minElement = heapq.heappop(heap1)
largeElement = heapq.nlargest(1,heap1)
twoLargeElements = heapq.nlargest(2,heap1)
smallestElement = heapq.nsmallest(2,heap1)
print(minElement)
print(twoLargeElements)
print(largeElement)
print(smallestElement)

print(heap1)

# heap2 = [1,2,3,4,5]
# heapq.heapify(heap2)
# heapq.heappop(heap2)
# print(heap2)


