import sys
from collections import deque


input = sys.stdin.readline

in_n, in_m = map(int, input().split())
list_idx = list(map(int, input().split()))
que_n = deque(range(1, in_n + 1))
answer = 0
for idx in list_idx:

    cmd_2 = 0
    while que_n[cmd_2] != idx:
        cmd_2 += 1

    cmd_3 = 0
    while que_n[cmd_3] != idx:
        cmd_3 -= 1
    cmd_3 *= -1

    if cmd_2 < cmd_3:
        for _ in range(cmd_2):
            que_n.append(que_n.popleft())
        que_n.popleft()
        answer += cmd_2

    else:
        for _ in range(cmd_3):
            que_n.appendleft(que_n.pop())
        que_n.popleft()
        answer += cmd_3

print(answer)
