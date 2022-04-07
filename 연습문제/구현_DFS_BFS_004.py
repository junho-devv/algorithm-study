# 괄호 변환
from collections import deque

# round_brackets = input()
round_brackets = "()))((()"
temp_list = [0] * len(round_brackets)

answer = ""

for i in range(len(round_brackets)):
    if round_brackets[i] == '(':
        temp_list[i] += 1
    if round_brackets[i] == ')':
        temp_list[i] -= 1


def line_up_brackets(a_que):
    a_que.popleft()
    a_que.pop()

    for a in range(len(a_que)):

        if a_que[a] == '(':
            a_que[a] = ')'

        elif a_que[a] == ')':
            a_que[a] = '('

    a_result = ['(']
    for a in range(len(a_que)):
        a_result.append(a_que[a])
    a_result.append(')')
    b_que = deque()

    for a in range(len(a_result)):
        b_que.append(a_result[a])

    return b_que


def solution(v_que):

    global answer

    u_que = deque()

    if not v_que:
        return answer

    a_temp = 0

    while v_que:

        temp_val = v_que.popleft()

        if temp_val == '(':
            a_temp += 1
        if temp_val == ')':
            a_temp -= 1

        u_que.append(temp_val)

        if a_temp == 0:
            break

    u_que = line_up_brackets(u_que)

    while u_que:
        answer += str(u_que.popleft())

    return solution(v_que)


u = deque()
v = deque()

for i in range(len(round_brackets)):
    v.append(round_brackets[i])

print(solution(v))
