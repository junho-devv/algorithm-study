import sys


def fibonacci(para_n):
    answer = 1

    f_var1, f_var2 = 0, 1

    for p_ in range(1, para_n):
        answer = f_var1 + f_var2
        f_var1 = f_var2
        f_var2 = answer

    return answer


def fibonacci_recursion(para_n):
    if para_n == 1 or para_n == 2:
        return

    answer = fibonacci(para_n - 1) + fibonacci_recursion(para_n - 2)

    return answer


if __name__ == '__main__':
    in_n = int(sys.stdin.readline())

    out_1 = fibonacci(in_n)
    print(out_1)

    out_2 = fibonacci_recursion(in_n)
    print(out_2)
