def solution(N):

    dynamic_table = [0] * (10 ** 2 + 1)

    for i in range(1, 4):
        dynamic_table[i] = 1

    for idx in range(4, N + 1):
        dynamic_table[idx] = dynamic_table[idx - 2] + dynamic_table[idx - 3]

    answer = dynamic_table[N]
    return answer


if __name__ == "__main__":

    import sys

    in_tc = int(sys.stdin.readline())

    for _ in range(in_tc):
        in_n = int(sys.stdin.readline())

        print(solution(in_n))
