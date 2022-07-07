from collections import deque
import sys


que_1 = []
for _ in range(3):
    in_ = int(sys.stdin.readline())
    que_1.append(in_)
que_1.pop(0)

print(que_1)