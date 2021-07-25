def solution():
    # 숫자 X(input_x) 입력받기
    input_x = int(input())

    stack_x = 1

    while True:
        sum_x = stack_x * (stack_x + 1) // 2

        if sum_x >= input_x:
            result_x = stack_x
            break
        else:
            stack_x += 1

    start_x = sum_x - result_x
    ord_x = input_x - start_x

    if stack_x % 2 == 0:
        denom_x, numer_x = result_x - ord_x + 1, ord_x
    else:
        denom_x, numer_x = ord_x, result_x - ord_x + 1

    answer = str(numer_x) + "/" + str(denom_x)

    print(answer)


def solution_1():
    input_x = int(input())
    stack_x = 1

    while input_x > stack_x:
        input_x -= stack_x
        stack_x += 1

    if stack_x % 2 == 0:
        dividend_x = input_x
        divisor_x = stack_x - input_x + 1
    else:
        dividend_x = stack_x - input_x + 1
        divisor_x = input_x

    print("{}/{}".format(dividend_x, divisor_x))


solution_1()
