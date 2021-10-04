import sys

input = sys.stdin.readline

in_n = int(input())
list_n = list(map(int, input().split()))
in_m = int(input())
list_m = list(map(int, input().split()))


def binary_search(para_left, para_right, para_val):
    if para_left > para_right:
        return 0

    the_mid = (para_left + para_right) // 2
    if list_n[the_mid] == para_val:
        return 1
    else:
        if list_n[the_mid] > para_val:
            return binary_search(para_left, the_mid - 1, para_val)
        else:
            return binary_search(the_mid + 1, para_right, para_val)


list_n.sort()
for m in list_m:
    print(binary_search(0, in_n - 1, m))
