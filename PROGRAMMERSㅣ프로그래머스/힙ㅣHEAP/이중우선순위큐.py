def solution(operations):

    import heapq

    heap_min = []
    heap_max = []

    for operation in operations:
        op_1, op_2 = operation.split()

        if op_1 == "I":
            heapq.heappush(heap_min, int(op_2))
            heapq.heappush(heap_max, (int(op_2) * -1, int(op_2)))

        else:
            if not heap_min:
                pass

            elif op_2 == "1":
                max_num = heapq.heappop(heap_max)[1]
                heap_min.remove(max_num)

            elif op_2 == "-1":
                min_num = heapq.heappop(heap_min)
                heap_max.remove((min_num * -1, min_num))

    if heap_min:
        answer = [heapq.heappop(heap_max)[1], heapq.heappop(heap_min)]
    else:
        answer = [0, 0]

    return answer


def solution_1(operations):

    import heapq

    heap_num = []

    for operation in operations:
        op_1, op_2 = operation.split()
        print(heap_num)
        if op_1 == "I":
            heapq.heappush(heap_num, int(op_2))

        else:
            if not heap_num:
                pass

            elif op_2 == "1":
                heap_num.pop()

            elif op_2 == "-1":
                heapq.heappop(heap_num)



if __name__ == '__main__':

    in_o = 	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

    print(solution_1(in_o))
