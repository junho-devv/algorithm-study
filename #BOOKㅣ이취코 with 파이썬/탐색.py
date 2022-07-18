def sequential_search(num, tar, arr):
    for x in range(num):
        if arr[x] == tar:
            return x + 1


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

    n, target = map(int, input().split())
    aList = list(map(int, input().split()))

    aResult = binary_search(aList, target, 0, n - 1)

    if aResult is None:
        print("해당 값이 없습니다.")
    else:
        print(aResult)
