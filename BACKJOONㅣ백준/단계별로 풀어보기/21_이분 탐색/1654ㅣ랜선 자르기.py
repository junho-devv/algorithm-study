import sys


def count_lan(para_list, para_val):
    num_lan = 0
    for one in para_list:
        num_lan += one // para_val

    return num_lan


def binary_search(para_left, para_right, para_list, para_n):
    answer = 0

    while para_left <= para_right:
        center = (para_left + para_right) // 2

        if count_lan(para_list, center) < para_n:
            para_right = center - 1
        else:
            answer = max(answer, center)
            para_left = center + 1

    return answer


if __name__ == '__main__':
    in_k, in_n = map(int, sys.stdin.readline().split())

    list_k = []
    for _ in range(in_k):
        list_k.append(int(sys.stdin.readline()))

    out_1 = binary_search(1, max(list_k), list_k, in_n)
    print(out_1)
