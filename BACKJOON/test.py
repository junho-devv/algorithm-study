import heapq


n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

print(heap)

result = 0

while True:

    if len(heap) == 1:
        break

    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    a_sum = one + two
    heapq.heappush(heap, a_sum)
    result += a_sum

print(result)
