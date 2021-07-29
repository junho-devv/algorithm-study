# 무수히 큰 수(INF)
INF = int(1e9)


def solution():
    # 설탕의 무게(weight_x) 입력받기
    weight_x = int(input())

    arr_x = [INF] * (weight_x + 1)

    arr_x[0] = 0

    for i in range(len(arr_x)):
        if arr_x[i] != INF and (i + 3) < len(arr_x):
            arr_x[i + 3] = arr_x[i] + 1 if arr_x[i + 3] > arr_x[i] else arr_x[i + 3]
        if arr_x[i] != INF and (i + 5) < len(arr_x):
            arr_x[i + 5] = arr_x[i] + 1 if arr_x[i + 5] > arr_x[i] else arr_x[i + 5]

    if arr_x[weight_x] == INF:
        print(-1)
    else:
        print(arr_x[weight_x])


solution()
