import sys
from collections import deque


input = sys.stdin.readline

num_tc = int(input())
for _ in range(num_tc):
    list_func = list(input())

    in_n = int(input())

    if in_n == 0:
        que_n = deque()
    else:
        que_n = deque(input()[1: -2].split(','))

    error = False
    count_r = 0
    for func in list_func:
        if func == 'R':
            count_r += 1

        elif func == 'D':
            if not que_n:
                error = True
                break
            else:
                if count_r % 2:
                    que_n.pop()
                else:
                    que_n.popleft()

    if count_r % 2:
        que_n.reverse()

    if error:
        print("error")
    else:
        answer = "[" + ','.join(que_n) + "]"
        print(answer)
