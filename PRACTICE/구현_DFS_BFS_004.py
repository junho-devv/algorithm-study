# 괄호 변환
from collections import deque

round_brackets = input()

temp_list = [0] * len(round_brackets)

for i in range(len(round_brackets)):
    if round_brackets[i] == '(':
        temp_list[i] += 1
    if round_brackets[i] == ')':
        temp_list[i] -= 1

u = deque()
v = deque()

for i in range(len(round_brackets)):
    v.append(round_brackets[i])

temp = 0

for i in range(len(round_brackets)):
    temp += temp_list[i]

    u.append(v.popleft())

    if temp == 0:
        break

print(u, v)
