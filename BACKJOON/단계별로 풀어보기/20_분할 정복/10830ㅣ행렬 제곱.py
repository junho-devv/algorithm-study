import sys


input = sys.stdin.readline

in_n, in_b = map(int, input().split())
matrix_a = []
for _ in range(in_n):
    matrix_a.append(list(map(int, input().split())))


def multiple(para_matrix_a, para_matrix_b):
    matrix_result = [[0 for _ in range(in_n)] for _ in range(in_n)]
    for row in range(in_n):
        for col in range(in_n):
            for k in range(in_n):
                matrix_result[row][col] += para_matrix_a[row][k] * para_matrix_b[k][col]
            matrix_result[row][col] %= 1000

    return matrix_result


def power(para_b):
    if para_b == 1:
        return matrix_a

    if para_b % 2:
        power_b = power(para_b // 2)
        return multiple(multiple(power_b, power_b), matrix_a)

    else:
        power_b = power(para_b // 2)
        return multiple(power_b, power_b)


answer = power(in_b)

for ans in answer:
    for a in ans:
        print(a % 1000, end=' ')
    print()
