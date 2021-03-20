def sequential_search(num, tar, arr):
    for x in range(num):
        if arr[x] == tar:
            return x + 1


def binary_search(arr, tar, start, end):

    # if start > end:
    #     return None
    #
    # mid = (start + end) // 2
    #
    # if arr[mid] == tar:
    #     return mid + 1
    # elif arr[mid] > tar:
    #     return binary_search(arr, tar, start, mid - 1)
    # else:
    #     return binary_search(arr, tar, mid + 1, end)

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == tar:
            return mid + 1
        elif arr[mid] > tar:
            end = mid - 1
        else:
            start = mid + 1

    return None


# input_data = input().split()
# n = int(input_data[0])
# target = input_data[1]
#
# aList = input().split()
#
# print(sequential_search(n, target, aList))

n, target = map(int, input().split())
aList = list(map(int, input().split()))

aResult = binary_search(aList, target, 0, n - 1)

if aResult is None:
    print("해당 값이 없습니다.")
else:
    print(aResult)
