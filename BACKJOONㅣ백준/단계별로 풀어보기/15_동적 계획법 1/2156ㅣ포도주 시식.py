def solution(N, wines):

    dynamic_table = [0] * (10 ** 4 + 1)
    dynamic_table[1] = wines[1]
    dynamic_table[2] = wines[1] + wines[2]

    for i in range(3, N + 1):
        dynamic_table[i] = max(dynamic_table[i - 3] + wines[i - 1] + wines[i], dynamic_table[i - 2] + wines[i],
                               dynamic_table[i - 1])

    answer = dynamic_table[N]
    return answer


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())
    in_w = [0] + [int(sys.stdin.readline()) for _ in range(in_n)]

    print(solution(in_n, in_w))
