def solution(money):
    # 첫번째 집을 무조건 털면, 마지막 집은 선택권이 없다.
    dp_money_1 = [0] * len(money)
    dp_money_1[0] = money[0]

    for idx in range(1, len(money) - 1):
        dp_money_1[idx] = max(dp_money_1[idx - 1], dp_money_1[idx - 2] + money[idx])
    # 첫번째 집을 털지않고, 마지막 집에 선택권을 주게한다.
    dp_money_2 = [0] * len(money)
    dp_money_2[0] = 0

    for idx in range(1, len(money)):
        dp_money_2[idx] = max(dp_money_2[idx - 1], dp_money_2[idx - 2] + money[idx])

    # answer = max(max(dp_money_1), max(dp_money_2))
    answer = max(dp_money_1[-2], dp_money_2[-1])

    return answer


if __name__ == '__main__':
    in_m = [1, 2, 3, 1]

    solution(in_m)
