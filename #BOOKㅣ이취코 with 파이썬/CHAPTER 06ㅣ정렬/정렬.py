array = [7, 5, 9, 6, 3, 1, 2, 4, 8, 0]

for x in range(len(array)):
    miniValue = x
    for y in range(x + 1, len(array)):
        if array[miniValue] > array[y]:
            miniValue = y

    array[x], array[miniValue] = array[miniValue], array[x]

print("선택정렬 : ", array)

array = [7, 5, 9, 6, 3, 1, 2, 4, 8, 0]

for x in range(1, len(array)):
    for y in range(x, 0, -1):
        if array[y] < array[y - 1]:
            array[y], array[y - 1] = array[y - 1], array[y]
        else:
            break

print("삽입정렬 : ", array)


def quick_sort(num, start, end):

    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and num[left] < num[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and num[right] > num[pivot]:
            right -= 1

        if left > right:
            num[right], num[pivot] = num[pivot], num[right]
        else:
            num[left], num[right] = num[right], num[left]

    quick_sort(num, start, right - 1)
    quick_sort(num, right + 1, end)


arr = [7, 5, 9, 6, 3, 1, 2, 4, 8, 0]

quick_sort(arr, 0, len(arr) - 1)
print("퀵 정렬 : ", arr)


def quick_sort(inp):

    if len(inp) <= 1:
        return inp

    pivot = inp[0]
    tail = inp[1:]

    left_side = [a for a in tail if a <= pivot]
    right_side = [a for a in tail if a > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


arr002 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print("퀵 정렬 002 : ", quick_sort(arr002))

arr003 = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(arr003) + 1)

for i in range(len(arr003)):
    count[arr003[i]] += 1

arr04 = []
for i in range(len(count)):
    for j in range(count[i]):
        arr04.append(i)
print("계수정렬 : ", arr04)

arr005 = [('바나나', 2), ('사과', 5), ('당근', 3)]


def setting(data):
    return data[1]


result = sorted(arr005, key=setting)

print(result)
