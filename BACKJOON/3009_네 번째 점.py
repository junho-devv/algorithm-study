# 직사각형의 각 꼭지점을 저장할 배열(arr_x)
arr_a = []

# 세 개의 점 입력받기
for _ in range(3):
    arr_a.append(list(map(int, input().split())))

arr_x, arr_y = [], []
for i in arr_a:
    arr_x.append(i[0])
    arr_y.append(i[1])

min_x, max_x = min(arr_x), max(arr_x)
min_y, max_y = min(arr_y), max(arr_y)

for x in [min_x, max_x]:
    for y in [min_y, max_y]:

        if [x, y] not in arr_a:
            print(x, y)

