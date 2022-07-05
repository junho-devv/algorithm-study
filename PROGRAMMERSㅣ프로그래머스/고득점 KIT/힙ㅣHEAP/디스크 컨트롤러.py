def solution(jobs):

    sorted_jobs = sorted([(job[1], job[0]) for job in jobs], reverse=True, key=lambda e: (e[1], e[0]))

    import heapq

    que_jobs = []
    heapq.heappush(que_jobs, sorted_jobs.pop())

    now_time, total_time = 0, 0

    while que_jobs:
        temp_t, temp_s = heapq.heappop(que_jobs)
        now_time = max(now_time + temp_t, temp_s + temp_t)
        total_time += now_time - temp_s

        while sorted_jobs and sorted_jobs[-1][1] <= now_time:
            heapq.heappush(que_jobs, sorted_jobs.pop())
        if sorted_jobs and not que_jobs:
            heapq.heappush(que_jobs, sorted_jobs.pop())

    answer = total_time // len(jobs)

    return answer


if __name__ == '__main__':

    in_j = [[0, 3], [1, 9], [2, 6]]

    print(solution(in_j))
