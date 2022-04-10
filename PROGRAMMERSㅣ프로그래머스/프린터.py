from collections import deque


def solution(priorities, location):
    answer = 0

    que_priorities = deque(enumerate(priorities))
    print(que_priorities)

    temp_list = []
    while que_priorities:
        que_priorities.popleft()

    return answer


if __name__ == '__main__':
    in_p = [2, 1, 3, 2]
    in_l = 2

    solution(in_p, in_l)
