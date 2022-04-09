from math import ceil


def solution(progresses, speeds):
    answer = []

    list_time = []
    for progress, speed in zip(progresses, speeds):
        list_time.append(ceil((100 - progress) / speed))

    prev_idx = 0
    for i in range(len(list_time)):
        if list_time[i] > list_time[prev_idx]:
            answer.append(i - prev_idx)
            prev_idx = i
    answer.append(len(list_time) - prev_idx)

    return answer


if __name__ == '__main__':
    in_p = [95, 90, 99, 99, 80, 99]
    in_s = [1, 1, 1, 1, 1, 1]

    solution(in_p, in_s)
