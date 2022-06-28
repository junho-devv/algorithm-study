def solution(N):

    import heapq

    heap_que = []
    for _ in range(N):
        int_ = int(sys.stdin.readline())

        if int_ == 0:
            if len(heap_que) == 0:
                print(0)
            else:
                print(heapq.heappop(heap_que))
        else:
            heapq.heappush(heap_que, int_)


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    print(solution(in_n))
