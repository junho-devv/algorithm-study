def solution(N):

    dynamic_table = [0] * (int(1e6) + 1)
    dynamic_table[1] = 1
    dynamic_table[2] = 2

    for i in range(3, N + 1):
        dynamic_table[i] = (dynamic_table[i - 1] + dynamic_table[i - 2]) % 15746

    answer = dynamic_table[N]
    return answer


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    print(solution(in_n))
