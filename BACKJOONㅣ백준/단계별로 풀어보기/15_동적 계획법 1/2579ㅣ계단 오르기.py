def solution(N, scores):

    dynamic_table = [0] * 301

    dynamic_table[1] = scores[1]
    dynamic_table[2] = scores[1] + scores[2]

    for idx in range(3, N + 1):
        dynamic_table[idx] = max(dynamic_table[idx - 3] + scores[idx - 1] + scores[idx],
                                 dynamic_table[idx - 2] + scores[idx])

    answer = dynamic_table[N]
    return answer


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())
    in_s = [0] + [int(sys.stdin.readline()) for _ in range(in_n)]

    print(solution(in_n, in_s))
