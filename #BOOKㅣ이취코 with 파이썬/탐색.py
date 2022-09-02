def binary_search(arr, tar, start, end):

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == tar:
            return mid + 1

        elif arr[mid] > tar:
            end = mid - 1

        else:
            start = mid + 1

    return None


if __name__ == "__main__":

    import sys

    n, target = map(int, sys.stdin.readline().split())
    aList = list(map(int, sys.stdin.readline().split()))

    aResult = binary_search(aList, target, 0, n - 1)

    if aResult is None:
        print("해당 값이 없습니다.")
    else:
        print(aResult)
