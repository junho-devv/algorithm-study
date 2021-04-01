from collections import deque
import copy

# 강의의 수 : c_num
c_num = int(input())

in_order = [0] * (c_num + 1)

course_list = [[] for _ in range(c_num + 1)]

cost_list = [0] * (c_num + 1)

for i in range(1, c_num + 1):
    a_input = list(map(int, input().split()))
    cost_list[i] = a_input[0]
    for j in a_input[1:-1]:
        in_order[i] += 1
        course_list[j].append(i)

print(course_list)
print(cost_list)


def topology_sort():

    a_result = copy.deepcopy(cost_list)
    a_que = deque()

    for x in range(1, c_num + 1):
        if in_order[x] == 0:
            a_que.append(x)

    while a_que:

        now = a_que.popleft()

        for x in course_list[now]:

            a_result[x] = max(a_result[x], cost_list[x] + a_result[now])

            in_order[x] -= 1

            if in_order[x] == 0:
                a_que.append(x)

    for x in range(1, c_num + 1):
        print(a_result[x])


topology_sort()

