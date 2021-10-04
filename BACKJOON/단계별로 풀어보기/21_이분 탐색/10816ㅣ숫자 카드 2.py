import sys

input = sys.stdin.readline

in_n = int(input())
list_n = list(map(int, input().split()))
in_m = int(input())
list_m = list(map(int, input().split()))


def binary_search(para_left, para_right, para_val):
    if para_left > para_right:
        return 0

    center = (para_left + para_right) // 2
    if list_n[center] == para_val:
        count_val = 1
        for i in reversed(range(para_left, center)):
            if list_n[i] == para_val:
                count_val += 1
            else:
                break
        for i in range(center + 1, para_right + 1):
            if list_n[i] == para_val:
                count_val += 1
            else:
                break

        return count_val

    else:
        if list_n[center] > para_val:
            return binary_search(para_left, center - 1, para_val)
        else:
            return binary_search(center + 1, para_right, para_val)


list_n.sort()
for m in list_m:
    print(binary_search(0, in_n - 1, m), end=' ')
