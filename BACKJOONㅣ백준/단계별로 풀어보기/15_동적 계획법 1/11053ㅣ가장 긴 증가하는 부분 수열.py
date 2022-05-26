def solution(len_n, seq_n):

    dynamic_table = [0] * (int(1e3) + 1)

    for l in range(len_n):
        for idx in range(l):
            if seq_n[l] > seq_n[idx] and dynamic_table[l] < dynamic_table[idx]:
                dynamic_table[l] = dynamic_table[idx]

        dynamic_table[l] += 1

    answer = max(dynamic_table)
    return answer


if __name__ == "__main__":

    import sys

    in_l = int(sys.stdin.readline())
    in_n = list(map(int, sys.stdin.readline().split()))

    print(solution(in_l, in_n))
