# 연산자 끼워 넣기

from itertools import permutations
from collections import deque

n_num = int(input())
n_list = list(map(int, input().split()))

# 덧셈(+), 뺄셈(-), 곱셈(X), 나눗셈(/)
o_num_list = list(map(int, input().split()))

result_list = []


def calculate_result(n_que, o_que):

    answer = n_que.popleft()

    while o_que:

        a_operator = o_que.popleft()
        a_next = n_que.popleft()

        if a_operator == 0:
            answer += a_next
        if a_operator == 1:
            answer -= a_next
        if a_operator == 2:
            answer *= a_next
        if a_operator == 3:
            if answer > 0:
                answer //= a_next
            else:
                answer *= -1
                answer //= a_next
                answer *= -1

    return answer


def solution():

    o_list = deque()
    for i in range(4):
        if o_num_list[i] > 0:
            for j in range(o_num_list[i]):
                o_list.append(i)

    max_result = (-1) * int(1e9)
    min_result = int(1e9)

    candidates = list(permutations(o_list, len(o_list)))
    for candidate in candidates:

        n_que = deque()
        for x in range(n_num):
            n_que.append(n_list[x])

        a_result = calculate_result(n_que, deque(candidate))

        max_result = max(max_result, a_result)
        min_result = min(min_result, a_result)

    print(max_result)
    print(min_result)


solution()
