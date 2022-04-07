import sys
import heapq


in_n = int(sys.stdin.readline())
heap_left, heap_right = [], []
for _ in range(in_n):
    temp_int = int(sys.stdin.readline())

    if len(heap_left) == len(heap_right):
        heapq.heappush(heap_left, (-temp_int, temp_int))
    else:
        heapq.heappush(heap_right, (temp_int, temp_int))

    if heap_right and heap_left[0][1] > heap_right[0][1]:
        pop_left = heapq.heappop(heap_left)[1]
        pop_right = heapq.heappop(heap_right)[1]
        heapq.heappush(heap_right, (pop_left, pop_left))
        heapq.heappush(heap_left, (-pop_right, pop_right))

    print(heap_left[0][1])
