def solution(num_n, seq_n):

    dynamic_table_1 = [0] * (int(1e3) + 1)
    dynamic_table_2 = [0] * (int(1e3) + 1)

    for x in range(num_n):
        for y in range(x):
            if seq_n[x] > seq_n[y] and dynamic_table_1[x] < dynamic_table_1[y]:
                dynamic_table_1[x] = dynamic_table_1[y]
        dynamic_table_1[x] += 1

    for x in reversed(range(num_n)):
        for y in range(num_n - 1, x, -1):
            if seq_n[x] > seq_n[y] and dynamic_table_2[x] < dynamic_table_2[y]:
                dynamic_table_2[x] = dynamic_table_2[y]
        dynamic_table_2[x] += 1

    sum_dynamic_table = [0] * (int(1e3) + 1)

    for i in range(num_n):
        sum_dynamic_table[i] = dynamic_table_1[i] + dynamic_table_2[i] - 1

    answer = max(sum_dynamic_table)
    return answer


if __name__ == "__main__":

    import sys

    num_n = int(sys.stdin.readline())
    seq_n = list(map(int, sys.stdin.readline().split()))

    # print(solution(num_n, seq_n))
