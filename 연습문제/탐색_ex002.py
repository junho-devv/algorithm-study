# n은 떡의 개수, m은 떡의 길이
n, m = map(int, input().split())

dList = list(map(int, input().split()))
dMax = max(dList)


def search_height(array, target, start, end):

    while start <= end:

        mid = (start + end) // 2
        d_sum = 0

        for x in array:
            if x - mid > 0:
                d_sum += x - mid

        if d_sum == target:
            return mid
        elif d_sum < target:
            end = mid - 1
        else:
            start = mid + 1

    return None


aResult = search_height(dList, m, 0, dMax)

if aResult is None:
    print("값이 존재하지 않습니다.")
else:
    print(aResult)