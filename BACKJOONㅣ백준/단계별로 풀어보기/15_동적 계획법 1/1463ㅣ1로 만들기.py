def solution(X):

    dynamic_table = [n - 1 for n in range(10 ** 6 + 1)]

    for i in range(2, X + 1):

        if i % 2 == 0:
            dynamic_table[i] = min(dynamic_table[i], dynamic_table[i // 2] + 1)

        if i % 3 == 0:
            dynamic_table[i] = min(dynamic_table[i], dynamic_table[i // 3] + 1)

        dynamic_table[i] = min(dynamic_table[i], dynamic_table[i - 1] + 1)

    answer = dynamic_table[X]
    return answer


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    print(solution(in_n))
