def fibonacci(para_n):
    if para_n == 1 or para_n == 2:
        return 1

    return fibonacci(para_n - 1) + fibonacci(para_n - 2)


if __name__ == '__main__':

    print(fibonacci(4))
