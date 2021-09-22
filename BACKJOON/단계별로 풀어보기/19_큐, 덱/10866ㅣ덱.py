import sys
from collections import deque


input = sys.stdin.readline

in_n = int(input())
que_n = deque()
for _ in range(in_n):
    cmd = input().split()

    if cmd[0] == 'push_front':
        que_n.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        que_n.append(cmd[1])

    elif cmd[0] == 'size':
        print(len(que_n))
    elif cmd[0] == 'empty':
        if not que_n:
            print(1)
        else:
            print(0)
    elif not que_n:
        print(-1)
    elif cmd[0] == 'pop_front':
        print(que_n.popleft())
    elif cmd[0] == 'pop_back':
        print(que_n.pop())
    elif cmd[0] == 'front':
        print(que_n[0])
    elif cmd[0] == 'back':
        print(que_n[-1])
