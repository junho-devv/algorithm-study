def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    print(factorial(5))
