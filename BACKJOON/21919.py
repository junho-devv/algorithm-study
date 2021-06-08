# 소수의 최소공배수
len_x = int(input())
seq_x = map(int, input().split())


def is_it_decimal_number(a_num):
    # 약수의 개수(num_m)
    num_m = 0

    for i in range(1, a_num + 1):
        if a_num % i == 0:
            num_m += 1
    # 소수는 약수의 개수가 자기자신과 1뿐, 고로 약수의 개수는 2개이다
    # 약수의 개수가 2개일 때
    if num_m == 2:
        return True
    # 약수의 개수가 2개 이상일 때
    else:
        return False


def solution():

    answer = 1

    for i in seq_x:
        if is_it_decimal_number(i):
            answer *= i

    if answer == 1:
        return -1
    else:
        return answer


print(solution())
