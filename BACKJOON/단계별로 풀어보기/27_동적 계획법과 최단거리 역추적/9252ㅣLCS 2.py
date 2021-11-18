import sys


def solution():
    in_a = [''] + list(sys.stdin.readline().rstrip())
    in_b = [''] + list(sys.stdin.readline().rstrip())

    len_a, len_b = len(in_a) - 1, len(in_b) - 1
    dp_ab = [[0 for _ in range(len_b + 1)] for _ in range(len_a + 1)]
    dp_ab2 = [["" for _ in range(len_b + 1)] for _ in range(len_a + 1)]
    for x in range(1, len_a + 1):
        for y in range(1, len_b + 1):
            if in_a[x] == in_b[y]:
                if dp_ab[x - 1][y] + 1 > dp_ab[x][y - 1]:
                    dp_ab[x][y] = max(dp_ab[x - 1][y] + 1, dp_ab[x][y - 1])
                    dp_ab2[x][y] = dp_ab2[x - 1][y] + in_a[x]
                else:
                    dp_ab[x][y] = dp_ab[x][y - 1]
                    dp_ab2[x][y] = dp_ab2[x][y - 1]
            else:
                if dp_ab[x - 1][y] > dp_ab[x][y - 1]:
                    dp_ab[x][y] = max(dp_ab[x - 1][y], dp_ab[x][y - 1])
                    dp_ab2[x][y] = dp_ab2[x - 1][y]
                else:
                    dp_ab[x][y] = dp_ab[x][y - 1]
                    dp_ab2[x][y] = dp_ab2[x][y - 1]
    for ab in dp_ab:
        print(*ab)
    for ab in dp_ab2:
        print(*ab)

    print(dp_ab[len_a][len_b])
    print(dp_ab2[len_a][len_b])
    return


if __name__ == '__main__':
    solution()
