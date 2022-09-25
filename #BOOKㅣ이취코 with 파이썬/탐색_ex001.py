def binary_search(arr, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


if __name__ == "__main__":

    import sys

    n = int(sys.stdin.readline())
    nList = list(map(int, sys.stdin.readlinet().split()))
    m = int(sys.stdin.readline())
    mList = list(map(int, sys.stdin.readline().split()))

    nList.sort()

    rList = []
    for x in mList:
        aResult = binary_search(nList, x, 0, n - 1)
        if aResult is None:
            rList.append('No')
        else:
            rList.append('Yes')

    print(rList)
