from collections import deque

# 강의의 수 : c_num
c_num = int(input())

course_list = [[] for _ in range(c_num + 1)]

for i in range(1, c_num + 1):
    course_list[i].append(list(map(int, input().split())))

print(course_list)

in_order = [0] * (c_num + 1)

for i in range(1, c_num + 1):
    in_order[i] = len(course_list[i]) - 2

def topology_sort():

    a_result = []
    a_que = deque()

    for x in range(1, c_num + 1):
        if in_order[x] == 0:
            a_que.append(x)

    while a_que:

        now = a_que.popleft()
        a_result.append(now)

        for x in course_list[now]



# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1
