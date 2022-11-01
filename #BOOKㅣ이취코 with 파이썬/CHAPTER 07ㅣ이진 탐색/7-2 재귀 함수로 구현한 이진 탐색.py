import sys


def binary_search(array, target, start, end):

    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


in_n, in_t = list(map(int, sys.stdin.readline().split()))
in_a = list(map(int, sys.stdin.readline().split()))

answer = binary_search(in_a, in_t, 0, in_n - 1)
if answer is None:
    print("원소가 존재하지 않습니다.")
else:
    print(answer + 1)
