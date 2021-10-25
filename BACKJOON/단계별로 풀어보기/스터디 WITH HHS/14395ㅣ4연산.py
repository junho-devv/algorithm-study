import sys
from collections import deque

in_s, in_t = map(int, sys.stdin.readline().split())
visited_s = set()
answer = ""


def operate(para_int, para_answer):
    que_s = deque([[para_int, para_answer]])

    while que_s:
        temp_int, temp_answer = que_s.popleft()

        if temp_int == in_t:
            return temp_answer

        for op in ['*', '+', '/']:
            if op == '*':
                temp_result = temp_int * temp_int
            elif op == '+':
                temp_result = temp_int + temp_int
            else:
                temp_result = 1

            if 0 <= temp_result <= in_t and temp_result not in visited_s:
                visited_s.add(temp_result)
                que_s.append([temp_result, temp_answer + op])
    return -1


if in_s == in_t:
    print(0)
else:
    visited_s.add(in_s)
    print(operate(in_s, ""))
