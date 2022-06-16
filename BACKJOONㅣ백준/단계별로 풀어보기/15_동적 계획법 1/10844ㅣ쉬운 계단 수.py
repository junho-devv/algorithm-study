def solution(N):

    dynamic_table = [[0] * 10 for _ in range(101)]

    for idx_1 in range(2, N + 1):
        for idx_2 in range(10):

            if idx_2 == 0:
                dynamic_table[idx_1][idx_2] = dynamic_table[idx_1 - 1][1]
            elif idx_2 == 9:
                dynamic_table[idx_1][idx_2] = dynamic_table[idx_1 - 1][8]
            else:
                dynamic_table[idx_1][idx_2] = dynamic_table[idx_1 - 1][idx_2 - 1] + dynamic_table[idx_1 - 1][idx_2 + 1]

    answer = sum(dynamic_table[N]) % 10 ** 9
    return answer


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    print(solution(in_n))
