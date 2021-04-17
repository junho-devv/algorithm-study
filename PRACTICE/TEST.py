from collections import deque

que = deque()

que.append(1)
que.append(2)
que.append(3)

que.pop()

b_que = deque()

b_que.append(5)
b_que.append(10)

que = b_que

b_que.popleft()

print(que)
