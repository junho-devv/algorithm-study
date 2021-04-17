# 연산자 끼워 넣기

from itertools import permutations
from collections import deque

n_num = int(input())
n_list = list(map(int, input().split()))
# 덧셈(+), 뺄셈(-), 곱셈(X), 나눗셈(/)
o_num_list = list(map(int, input().split()))
o_list = []

for i in range(4):
    if o_num_list[i] > 0:
        for j in range(o_num_list[i]):
            o_list.append(i)

candidates = list(permutations(o_list, len(o_list)))

result_list = []


def solution(start, operator, next_val):

    if operator == 0:
        start += next_val
    if operator == 1:
        start -= next_val
    if operator == 2:
        start *= next_val
    if operator == 3:
        if start > 0:
            start //= next_val
        else:
            start *= -1
            start //= next_val
            start *= -1

    return solution(start, )


print(solution(n_list[0], o_list[0], n_list[1]))

