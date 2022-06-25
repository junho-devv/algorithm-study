def solution(N, M, numbers):

    answer = 0

    for idx_1 in range(N):
        for idx_2 in range(idx_1 + 1, N):
            for idx_3 in range(idx_2 + 1, N):

                if numbers[idx_1] + numbers[idx_2] + numbers[idx_3] > M:
                    continue
                else:
                    answer = max(answer, numbers[idx_1] + numbers[idx_2] + numbers[idx_3])

    return answer


# # 조합을 활용한 풀이법
# def solution(N, M, numbers):
#
#     from itertools import combinations
#
#     combination_n = list(combinations(numbers, 3))
#
#     mini_n = int(1e9)
#
#     answer = []
#
#     for a in combination_n:
#
#         if 0 <= M - sum(a) < mini_n:
#             mini_n = M - sum(a)
#             answer = a
#
#     print(sum(answer))


if __name__ == "__main__":

    import sys

    in_n, in_m = map(int, sys.stdin.readline().split())
    in_l = list(map(int, sys.stdin.readline().split()))

    print(solution(in_n, in_m, in_l))

