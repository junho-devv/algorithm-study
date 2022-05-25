def solution(priorities, location):
    answer = 0

    from collections import deque

    que_priorities = deque([(priority, i) for i, priority in enumerate(priorities)])

    while que_priorities:

        document_j = que_priorities.popleft()

        if que_priorities and max(que_priorities)[0] > document_j[0]:
            que_priorities.append(document_j)

        else:
            answer += 1
            if document_j[1] == location:
                break

    return answer


if __name__ == '__main__':
    in_p = [1, 1, 9, 1, 1, 1]
    in_l = 0

    solution(in_p, in_l)
