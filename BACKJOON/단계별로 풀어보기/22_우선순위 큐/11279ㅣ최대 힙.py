import sys
import heapq


in_n = int(sys.stdin.readline())
heap_n = []
for _ in range(in_n):
    temp_int = int(sys.stdin.readline())

    if temp_int == 0:
        if not heap_n:
            print(0)
        else:
            print(-heapq.heappop(heap_n))
    else:
        heapq.heappush(heap_n, -temp_int)
