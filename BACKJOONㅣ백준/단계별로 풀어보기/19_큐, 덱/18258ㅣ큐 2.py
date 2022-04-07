import sys
from collections import deque


input = sys.stdin.readline
# 명령의 수(in_n) 입력받기
in_n = int(input())
que_n = deque()
for _ in range(in_n):
    cmd = input().split()

    if cmd[0] == 'push':
        que_n.append(cmd[1])

    elif cmd[0] == 'pop':
        if not que_n:
            print(-1)
        else:
            print(que_n.popleft())

    elif cmd[0] == 'size':
        print(len(que_n))

    elif cmd[0] == 'empty':
        if not que_n:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'front':
        if not que_n:
            print(-1)
        else:
            print(que_n[0])

    elif cmd[0] == 'back':
        if not que_n:
            print(-1)
        else:
            print(que_n[-1])
