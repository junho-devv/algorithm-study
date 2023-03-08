def fibonacci(para_n):

    print('f(' + str(para_n) + ')')

    if para_n == 1 or para_n == 2:
        return 1

    if dynamic_table[para_n] != 0:
        return dynamic_table[para_n]
    else:
        dynamic_table[para_n] = fibonacci(para_n - 1) + fibonacci(para_n - 2)
        return dynamic_table[para_n]


if __name__ == '__main__':

    dynamic_table = [0] * int(1e9)

    fibonacci(6)
