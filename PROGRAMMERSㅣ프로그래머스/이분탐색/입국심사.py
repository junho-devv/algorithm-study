def solution(n, times):

    time_s, time_e = 0, n * times[0]
    while time_s <= time_e:
        time_m = (time_s + time_e) // 2

        temp_cnt = 0
        for time in times:
            temp_cnt += time_m // time

        print(time_m, temp_cnt)
        if temp_cnt >= n:
            time_e = time_m - 1
        else:
            time_s = time_m + 1
    print(time_s, time_m, time_e)
    answer = time_s

    return answer


if __name__ == '__main__':
    in_n = 6
    in_t = [7, 10, 3]

    solution(in_n, in_t)
