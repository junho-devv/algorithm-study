import sys
import heapq


in_n = int(sys.stdin.readline())
heap_n = []
for _ in range(in_n):
    int_n = int(sys.stdin.readline())
    if int_n == 0:
        if len(heap_n) == 0:
            print(0)
        else:
            print(heapq.heappop(heap_n)[1])
    else:
        heapq.heappush(heap_n, (abs(int_n), int_n))
