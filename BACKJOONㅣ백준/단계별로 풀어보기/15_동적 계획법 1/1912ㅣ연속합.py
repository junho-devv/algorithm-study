def solution(N, sequence):

    dynamic_table = [0] * (10 ** 5 + 1)

    for i in range(N):
        if dynamic_table[i] < 0:
            dynamic_table[i + 1] = sequence[i]
        else:
            dynamic_table[i + 1] = dynamic_table[i] + sequence[i]

    answer = max(dynamic_table[1: N + 1])
    return answer


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())
    in_s = list(map(int, sys.stdin.readline().split()))

    print(solution(in_n, in_s))
