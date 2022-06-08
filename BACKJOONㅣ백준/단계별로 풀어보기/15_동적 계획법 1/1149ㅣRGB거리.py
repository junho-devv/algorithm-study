if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    dynamic_table = [[0, 0, 0] for _ in range(int(1e3) + 1)]

    for i in range(1, in_n + 1):
        red, green, blue = map(int, input().split())

        dynamic_table[i][0] = min(dynamic_table[i - 1][1] + red, dynamic_table[i - 1][2] + red)
        dynamic_table[i][1] = min(dynamic_table[i - 1][2] + green, dynamic_table[i - 1][0] + green)
        dynamic_table[i][2] = min(dynamic_table[i - 1][0] + blue, dynamic_table[i - 1][1] + blue)

    print(min(dynamic_table[in_n]))
