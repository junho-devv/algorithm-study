def solution(scoville, K):

    import heapq

    heapq.heapify(scoville)
    answer = 0

    while len(scoville) > 1:

        hot_f = heapq.heappop(scoville)
        hot_s = heapq.heappop(scoville)

        if hot_f >= K:
            break

        mix_fs = hot_f + (hot_s * 2)

        heapq.heappush(scoville, mix_fs)
        answer += 1

    else:
        if scoville[0] >= K:
            return answer
        else:
            answer = -1

    return answer


if __name__ == '__main__':

    in_s = [1, 2, 3, 9, 10, 12]
    in_k = 7

    print(solution(in_s, in_k))
