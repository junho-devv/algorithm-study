def search_height(array, target, start, end):

    answer = 0

    while start <= end:

        mid = (start + end) // 2

        leftover = 0
        for h in array:
            if h > mid:
                leftover += h - mid

        if leftover < target:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    return answer


if __name__ == "__main__":

    import sys

    in_n, in_m = map(int, sys.stdin.readline().split())
    in_h = list(map(int, sys.stdin.readline().split()))

    print(search_height(in_h, in_m, 0, max(in_h)))
