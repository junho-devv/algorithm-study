import sys
from collections import deque


input = sys.stdin.readline

que_n = deque(input()[1: -2].split(','))
que_2n = deque()
print(que_n)
print(que_2n)