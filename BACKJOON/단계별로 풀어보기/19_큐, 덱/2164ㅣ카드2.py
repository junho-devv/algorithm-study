from collections import deque

in_n = int(input())
que_n = deque()
for i in range(in_n):
    que_n.append(i + 1)

while len(que_n) != 1:

    que_n.popleft()

    que_n.append(que_n.popleft())

print(que_n[0])
