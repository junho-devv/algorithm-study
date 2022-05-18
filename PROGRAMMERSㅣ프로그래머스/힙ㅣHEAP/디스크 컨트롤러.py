def solution(jobs):

    import heapq

    heap_jobs = []

    answer = 0
    time_s, time_e = -1, 0
    cnt_work = 0

    while cnt_work < len(jobs):

        for job in jobs:
            if time_s < job[0] <= time_e:
                heapq.heappush(heap_jobs, [job[1], job[0]])

        if len(heap_jobs) > 0:
            temp_work = heapq.heappop(heap_jobs)

            time_s = time_e
            time_e += temp_work[0]

            cnt_work += 1

            answer += time_e - temp_work[1]

        else:
            time_s += 1

    answer //= len(jobs)

    return answer


if __name__ == '__main__':

    in_j = [[0, 3], [1, 9], [2, 6]]

    print(solution(in_j))
