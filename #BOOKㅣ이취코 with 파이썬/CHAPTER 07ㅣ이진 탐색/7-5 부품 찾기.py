import sys


def binary_search(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


in_n = int(sys.stdin.readline())
in_cn = list(map(int, sys.stdin.readline().split()))

in_cn.sort()

in_m = int(sys.stdin.readline())
in_cm = list(map(int, sys.stdin.readline().split()))


for c in in_cm:
    answer = binary_search(in_cn, c, 0, in_n - 1)
    if answer is None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
