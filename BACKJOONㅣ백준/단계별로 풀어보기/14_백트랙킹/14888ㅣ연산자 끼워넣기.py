def solution(n, sequence, operators):

    def depth_first_search(depth, result, op_0, op_1, op_2, op_3):

        nonlocal maximum, minimum

        if depth == n:
            maximum = max(maximum, result)
            minimum = min(minimum, result)
            return

        if op_0:
            depth_first_search(depth + 1, result + sequence[depth], op_0 - 1, op_1, op_2, op_3)

        if op_1:
            depth_first_search(depth + 1, result - sequence[depth], op_0, op_1 - 1, op_2, op_3)

        if op_2:
            depth_first_search(depth + 1, result * sequence[depth], op_0, op_1, op_2 - 1, op_3)

        if op_3:
            depth_first_search(depth + 1, result // sequence[depth], op_0, op_1, op_2, op_3 - 1)

    maximum = int(1e9) * -1
    minimum = int(1e9)

    depth_first_search(1, sequence[0], operators[0], operators[1], operators[2], operators[3])

    print(maximum)
    print(minimum)


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())
    in_a = list(map(int, sys.stdin.readline().split()))
    in_o = list(map(int, sys.stdin.readline().split()))

    solution(in_n, in_a, in_o)
