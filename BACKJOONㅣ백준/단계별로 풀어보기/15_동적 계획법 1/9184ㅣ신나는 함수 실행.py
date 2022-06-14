def solution(A, B, C):

    def w(a, b, c):

        if a <= 0 or b <= 0 or c <= 0:
            return 1

        elif a > 20 or b > 20 or c > 20:
            return w(20, 20, 20)

        elif dynamic_table[a][b][c]:
            return dynamic_table[a][b][c]

        elif a < b < c:
            dynamic_table[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return dynamic_table[a][b][c]

        else:
            dynamic_table[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
            return dynamic_table[a][b][c]

    answer = f"w({A}, {B}, {C}) = {w(A, B, C)}"
    return answer


if __name__ == "__main__":

    import sys

    dynamic_table = [[[0] * 21 for _ in range(21)] for _ in range(21)]

    while True:

        in_a, in_b, in_c = map(int, sys.stdin.readline().split())

        if in_a == in_b == in_c == -1:
            break

        print(solution(in_a, in_b, in_c))
