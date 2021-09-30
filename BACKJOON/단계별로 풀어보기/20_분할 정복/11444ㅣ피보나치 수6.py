import sys

input = sys.stdin.readline

in_n = int(input())
fibonacci_n = [[1, 1], [1, 0]]
modulo_n = int(1e9) + 7


def multiple(para_matrix_a, para_matrix_b):
    matrix_result = [[0 for _ in range(2)] for _ in range(2)]
    for row in range(2):
        for col in range(2):
            for k in range(2):
                matrix_result[row][col] += para_matrix_a[row][k] * para_matrix_b[k][col] % modulo_n

    return matrix_result


def power(para_n):
    if para_n == 1:
        return fibonacci_n

    if para_n % 2:
        result = power(para_n // 2)
        result = multiple(result, result)
        result = multiple(result, fibonacci_n)

        return result

    else:
        result = power(para_n // 2)
        result = multiple(result, result)

        return result


answer = power(in_n)
print(answer[0][1] % modulo_n)

# [F_n+2, F_n+1] = [[1, 1], [1, 0]] * [F_n+1, F_n]
# As a result, [[F_n+1, F_n], [F_n, F_n-1]] = [[1, 1], [1, 0]] ** n

