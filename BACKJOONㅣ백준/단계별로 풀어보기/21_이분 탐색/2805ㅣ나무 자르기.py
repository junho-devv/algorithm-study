import sys


def cut(para_cut):
    answer = 0

    for tree in list_tree:
        if tree - para_cut > 0:
            answer += tree - para_cut

    return answer


def search():
    temp_low, temp_high = 1, max(list_tree)
    while temp_low <= temp_high:
        temp_m = (temp_low + temp_high) // 2
        if cut(temp_m) >= in_m:
            temp_low = temp_m + 1
        else:
            temp_high = temp_m - 1

    return temp_high


if __name__ == '__main__':
    in_n, in_m = map(int, sys.stdin.readline().split())
    list_tree = list(map(int, sys.stdin.readline().split()))

    print(search())
