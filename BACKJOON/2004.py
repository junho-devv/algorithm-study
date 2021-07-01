n, m = map(int, input().split())


def count_num_of_2(a_num):
    # a_num!에서 2의 개수(answer)
    answer = 0
    # a_num!에서 2의 개수(answer)를 구하기
    while a_num != 0:
        a_num = a_num // 2
        answer += a_num

    return answer


def count_num_of_5(a_num):
    # a_num!에서 5의 개수(answer)
    answer = 0
    # a_num!에서 5의 개수(answer)를 구하기
    while a_num != 0:
        a_num = a_num // 5
        answer += a_num

    return answer


def solution():
    if m == 0:
        answer = 0
    else:
        # 2의 개수와 5의 개수 중 적은 것의 개수로 초기화
        answer = min(count_num_of_2(n) - count_num_of_2(m) - count_num_of_2(n - m),
                     count_num_of_5(n) - count_num_of_5(m) - count_num_of_5(n - m))

    return answer


print(solution())

