import sys


def fibonacci(para_n):
    f_var1 = 0
    f_var2 = 1

    answer = 1

    for p_ in range(1, para_n):
        answer = f_var1 + f_var2
        f_var1 = f_var2
        f_var2 = answer

    return answer


if __name__ == '__main__':
    in_n = int(sys.stdin.readline())

    out_ = fibonacci(in_n)
    print(out_)
