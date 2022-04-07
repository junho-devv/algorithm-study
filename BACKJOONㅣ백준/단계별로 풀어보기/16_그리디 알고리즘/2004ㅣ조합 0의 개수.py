in_n, in_m = map(int, input().split())


def count_num_of_2(para_int):
    answer = 0

    while para_int != 0:
        para_int //= 2
        answer += para_int

    return answer


def count_num_of_5(para_int):
    answer = 0

    while para_int != 0:
        para_int //= 5
        answer += para_int

    return answer


result_nm = min(count_num_of_2(in_n) - count_num_of_2(in_m) - count_num_of_2(in_n - in_m),
                count_num_of_5(in_n) - count_num_of_5(in_m) - count_num_of_5(in_n - in_m))

print(result_nm)
