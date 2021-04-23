# 카드 정렬하기
from collections import deque


def solution(a_num, a_list):
    answer = 0

    a_list.sort()

    d_que = deque(a_list)

    a_index = 0
    while True:

        if a_index == a_num - 1:
            break

        a_list.sort()
        a_sum = a_list[a_index] + a_list[a_index + 1]
        a_list[a_index] = 0
        a_index += 1
        a_list[a_index] = a_sum

        answer += a_sum
    print(answer)
    return answer


d_num = int(input())
d_list = []
for _ in range(d_num):
    d_list.append(int(input()))

solution(d_num, d_list)
