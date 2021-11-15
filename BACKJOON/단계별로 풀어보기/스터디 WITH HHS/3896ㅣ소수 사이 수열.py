import sys


MAX = 1299709


def generate():
    temp_list = [False for _ in range(MAX + 1)]

    for n in range(2, MAX + 1):
        for m in range(n * n, MAX + 1, n):
            temp_list[m] = True

    answer = []
    for n in range(2, MAX + 1):
        if not temp_list[n]:
            answer.append(n)

    return temp_list, answer


def search(para_k):
    temp_l, temp_r = 0, len(list_pn2) - 1
    while temp_l < temp_r:
        print(temp_l, temp_r)
        temp_m = (temp_l + temp_r) // 2
        if list_pn2[temp_m] < para_k:
            temp_l = temp_m + 1
        else:
            temp_r = temp_m - 1

    return temp_l


if __name__ == '__main__':
    list_pn1, list_pn2 = generate()

    in_tc = int(sys.stdin.readline())
    for _ in range(in_tc):
        in_k = int(sys.stdin.readline())

        if not list_pn1[in_k]:
            print(0)
        else:
            idx_pn = search(in_k)
            print(list_pn2[idx_pn] - list_pn2[idx_pn - 1])
