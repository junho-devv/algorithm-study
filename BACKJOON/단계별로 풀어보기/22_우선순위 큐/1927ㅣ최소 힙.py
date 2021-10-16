import sys
import heapq


in_n = int(sys.stdin.readline())
heap_n = []
for _ in range(in_n):
    temp_n = int(sys.stdin.readline())
    if temp_n == 0:
        if len(heap_n) == 0:
            print(0)
        else:
            print(heapq.heappop(heap_n))
    else:
        heapq.heappush(heap_n, temp_n)
