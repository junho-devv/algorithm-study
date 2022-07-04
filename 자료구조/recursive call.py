def factorial_recursive(n):

    if n == 1:
        return 1

    return n * factorial_recursive(n-1)


def factorial_loop(n):

    answer = 1
    for idx in range(1, n + 1):
        answer *= idx

    return answer


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    print(factorial_loop(in_n))
