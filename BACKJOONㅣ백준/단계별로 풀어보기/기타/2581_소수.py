def solution():

    start_x = int(input())
    end_x = int(input())
    # 소수들의 합(sum_x), 최솟값(min_x)
    sum_x, min_x = 0, int(1e9)

    for i in range(start_x, end_x + 1):

        bool_x = True

        if i == 1:
            bool_x = False

        for j in range(2, i):
            if i % j == 0:
                bool_x = False

        if bool_x:
            sum_x += i
            min_x = min(min_x, i)

    if sum_x == 0:
        print(-1)
    else:
        print(sum_x)
        print(min_x)


solution()
