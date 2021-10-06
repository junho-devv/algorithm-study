from math import sqrt


def is_it_a_prime_number(a_num):

    if a_num == 2:
        return True

    for j in range(2, int(sqrt(a_num) + 1)):
        if a_num % j == 0:
            break
    else:
        return True

    return False


# 테스트 케이스의 개수(num_tc) 입력받기
num_tc = int(input())

for _ in range(num_tc):
    # 2보다 큰 임의의 짝수(even_x) 입력받기
    even_x = int(input())
    # even_x의 골드바흐 파티션을 담을 배열
    arr_x = []

    for i in range(2, even_x // 2 + 1):
        # even_x에서 i만큼 뺀 수
        num_x = even_x - i

        if is_it_a_prime_number(i) and is_it_a_prime_number(num_x):
            arr_x.append((i, num_x))

    diff_x = int(1e9)
    answer = 0
    for i in range(len(arr_x)):

        if arr_x[i][1] - arr_x[i][0] < diff_x:
            answer = i

    print("{} {}".format(arr_x[answer][0], arr_x[answer][1]))
