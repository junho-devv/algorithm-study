if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    dynamic_table = [0] * (in_n + 1)

    for x in range(2, in_n + 1):

        dynamic_table[x] = dynamic_table[x - 1] + 1

        if x % 2 == 0:
            dynamic_table[x] = min(dynamic_table[x], dynamic_table[x // 2] + 1)
        if x % 3 == 0:
            dynamic_table[x] = min(dynamic_table[x], dynamic_table[x // 3] + 1)
        if x % 5 == 0:
            dynamic_table[x] = min(dynamic_table[x], dynamic_table[x // 5] + 1)

    print(dynamic_table[in_n])
