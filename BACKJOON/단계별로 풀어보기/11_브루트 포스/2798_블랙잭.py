from itertools import combinations


def solution():

    input_n, input_m = map(int, input().split())

    arr_n = list(map(int, input().split()))

    combination_n = list(combinations(arr_n, 3))

    mini_n = int(1e9)

    answer = []

    for a in combination_n:

        if 0 <= input_m - sum(a) < mini_n:
            mini_n = input_m - sum(a)
            answer = a

    print(sum(answer))


solution()
