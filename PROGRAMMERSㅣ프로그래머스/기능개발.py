def solution(progresses, speeds):
    answer = []

    stack_r = [0]
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i]:
            r = (100 - progresses[i]) // speeds[i] + 1
        else:
            r = (100 - progresses[i]) // speeds[i]
        stack_r.append(r)
    prev_work = 0
    result = 0
    while stack_r:
        now_work = stack_r.pop()

        if prev_work <= now_work:
            result += 1

        else:
            answer.append(result)
            result = 1

        prev_work = now_work

    answer.reverse()

    return answer


if __name__ == '__main__':
    in_p = [95, 90, 99, 99, 80, 99]
    in_s = [1, 1, 1, 1, 1, 1]

    solution(in_p, in_s)