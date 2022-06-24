def solution():

    from itertools import combinations

    input_n, input_m = map(int, input().split())

    arr_n = list(map(int, input().split()))

    combination_n = list(combinations(arr_n, 3))

    mini_n = int(1e9)

    answer = []

    for a in combination_n:

        if 0 <= input_m - sum(a) < mini_n:
            mini_n = input_m - sum(a)
            answer = a

    print(sum(answer))


def solution_2(N, M, numbers):

    answer = 0

    for idx_1 in range(N):
        for idx_2 in range(idx_1 + 1, N):
            for idx_3 in range(idx_2 + 1, N):

                if numbers[idx_1] + numbers[idx_2] + numbers[idx_3] > M:
                    continue
                else:
                    answer = max(answer, numbers[idx_1] + numbers[idx_2] + numbers[idx_3])

    return answer


if __name__ == "__main__":

    import sys

    in_n, in_m = map(int, sys.stdin.readline().split())
    in_l = list(map(int, sys.stdin.readline().split()))

    print(solution_2(in_n, in_m, in_l))

