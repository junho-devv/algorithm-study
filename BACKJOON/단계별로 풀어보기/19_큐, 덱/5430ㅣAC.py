import sys
from collections import deque


input = sys.stdin.readline

# num_tc = int(input())
# for _ in range(num_tc):
#     funcs = list(input())
#
#     in_n = int(input())
#
#     que_n = input()
#     que_n = deque(que_n[1: -2].split(','))


# num_tc = int(input())
# for _ in range(num_tc):
#     funcs = list(input())
#
#     in_n = int(input())
#
#     que_n = input()
#     que_n = deque(que_n[1: -2].split(','))
#
#     error = False
#     if in_n - funcs.count('D') < 0:
#         error = True
#
#     for func in funcs:
#
#         if func == 'R':
#             reversed_n = deque()
#             for _ in range(in_n):
#                 reversed_n.append(que_n.pop())
#             for _ in range(in_n):
#                 que_n.append(reversed_n.popleft())
#
#         elif func == 'D':
#             if not que_n:
#                 error = True
#                 break
#             else:
#                 que_n.popleft()
#
#     if error:
#         print("error")
#     else:
#         answer = "[" + ','.join(que_n) + "]"
#         print(answer)
