def solution():
    # 숫자 N(input_n) 입력받기
    input_n = int(input())
    # 1 ~ 숫자 N 까지 최소거리(dist_n)
    dist_n = 1

    start_n, end_n, range_n = 1, 1, 0

    while True:

        if start_n <= input_n <= end_n:
            break

        else:
            range_n += 6
            start_n = end_n + 1
            end_n += range_n
            dist_n += 1

    print(dist_n)


solution()
