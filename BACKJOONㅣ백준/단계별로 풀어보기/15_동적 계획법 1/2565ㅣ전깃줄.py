def solution(N, wires):

    dynamic_table = [1] * 501

    for idx_1 in range(N):
        for idx_2 in range(idx_1):
            if wires[idx_1] > wires[idx_2] and dynamic_table[idx_1] < dynamic_table[idx_2] + 1:
                dynamic_table[idx_1] = dynamic_table[idx_2] + 1

    answer = N - max(dynamic_table)
    return answer


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    list_w = [list(map(int, sys.stdin.readline().split())) for _ in range(in_n)]

    print(solution(in_n, list_w))
