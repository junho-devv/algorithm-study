import sys
import heapq


in_n = int(sys.stdin.readline())

heap_que = []

for _ in range(in_n):

    int_ = int(sys.stdin.readline())

    if int_ == 0:
        if not heap_que:
            print(0)
        else:
            print(heapq.heappop(heap_que)[1])
    else:
        heapq.heappush(heap_que, (-int_, int_))
