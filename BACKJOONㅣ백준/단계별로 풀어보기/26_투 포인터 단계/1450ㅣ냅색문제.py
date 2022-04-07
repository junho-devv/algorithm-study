import sys


def brute_force(para_list1, para_list2, para_index, para_sum):
    if para_index >= len(para_list1):
        para_list2.append(para_sum)
        return

    # 현재 인덱스(para_index)의 물건의 무게를 더하지않을 때,
    brute_force(para_list1, para_list2, para_index + 1, para_sum)
    # 현재 인덱스(para_index)의 물건의 무게를 더할 때,
    brute_force(para_list1, para_list2, para_index + 1, para_sum + para_list1[para_index])


def binary_search(para_list, para_target, para_left, para_right):
    while para_left < para_right:
        middle = (para_left + para_right) // 2
        if para_list[middle] <= para_target:
            para_left = middle + 1
        else:
            para_right = middle

    return para_left


if __name__ == '__main__':
    in_n, in_c = map(int, sys.stdin.readline().split())
    stuff_n = list(map(int, sys.stdin.readline().split()))

    sub_1, sub_2 = stuff_n[:in_n // 2], stuff_n[in_n // 2:]
    sum_1, sum_2 = [], []

    brute_force(sub_1, sum_1, 0, 0)
    brute_force(sub_2, sum_2, 0, 0)

    num_case = 0
    sum_2.sort()
    for s in sum_1:
        if in_c - s < 0:
            continue
        num_case += binary_search(sum_2, in_c - s, 0, len(sum_2))

    print(num_case)
