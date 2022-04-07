from collections import deque


in_n, in_k = map(int, input().split())

que_n = deque([n for n in range(1, in_n + 1)])
answer = []

while que_n:
    for i in range(in_k - 1):
        que_n.append(que_n.popleft())
    answer.append(str(que_n.popleft()))

answer = "<" + ", ".join(answer) + ">"
print(answer)
