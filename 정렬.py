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
