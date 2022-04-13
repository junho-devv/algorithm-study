def solution(prices):
    answer = []

    for idx_1 in range(len(prices)):
        temp_time = 0
        for idx_2 in range(idx_1 + 1, len(prices)):
            temp_time += 1
            if prices[idx_1] > prices[idx_2]:
                break
        answer.append(temp_time)

    return answer


if __name__ == '__main__':
    in_p = [1, 2, 3, 2, 3]

    solution(in_p)
