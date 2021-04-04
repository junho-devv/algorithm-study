import heapq

food_times = list(map(int, input().split()))

k = int(input())

# pointer = 0
#
# for _ in range(k):
#
#     while food_times[pointer] == 0:
#         pointer += 1
#
#     if food_times[pointer] != 0:
#         food_times[pointer] -= 1
#         pointer += 1
#
#     pointer %= len(food_times)
#
# print(pointer + 1)


def solution():

    rest_food = sum(food_times)

    if rest_food <= k:
        return -1

    f_que = []

    for i in range(len(food_times)):
        heapq.heappush(f_que, (food_times[i], i + 1))

    sum_value = 0
    previous = 0

    length = len(food_times)

    while sum_value + ((f_que[0][0] - previous) * length) <= k:
        now = heapq.heappop(f_que)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(f_que, key=lambda x: x[1])
    print(result)
    return result[(k - sum_value) % length][1]


print(solution())
