while True:
    arr_x = list(map(int, input().split()))
    # 0, 0, 0이 입력된다면, 반복문 탈출
    if arr_x[0] == 0 and arr_x[1] == 0 and arr_x[2] == 0:
        break

    arr_x.sort()

    if arr_x[0] ** 2 + arr_x[1] ** 2 == arr_x[2] ** 2:
        print("right")
    else:
        print("wrong")


