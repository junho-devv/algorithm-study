import sys

input = sys.stdin.readline

in_n = int(input())
in_k = int(input())


def solution():
    list_a = [[row * col for col in range(1, in_n + 1)] for row in range(1, in_n + 1)]
    list_b = []
    for row in range(in_n):
        for col in range(in_n):
            list_b.append(list_a[row][col])
    list_b.sort()

    answer = list_b[in_k]
    print(answer)


solution()
