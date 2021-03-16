array = [7, 5, 9, 6, 3, 1, 2, 4, 8, 0]

for x in range(len(array)):
    miniValue = x
    for y in range(x+1, len(array)):
        if array[miniValue] > array[y]:
            miniValue = y

    array[x], array[miniValue] = array[miniValue], array[x]

print("선택정렬 : ", array)

array = [7, 5, 9, 6, 3, 1, 2, 4, 8, 0]

for x in range(1, len(array)):
    for y in range(x, 0, -1):
        if array[y] < array[y-1]:
            array[y], array[y-1] = array[y-1], array[y]
        else:
            break

print("삽입정렬 : ", array)

array = [7, 5, 9, 6, 3, 1, 2, 4, 8, 0]


def quick_sort(array, start, end):

    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] < array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] > array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print("퀵 정렬 : ", array)

