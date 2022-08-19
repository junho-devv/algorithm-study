def solution(N):

    answer = 0

    coins = [500, 100, 50, 10]

    for coin in coins:
        answer += N // coin
        N %= coin

    return answer


if __name__ == "__main__":

    import sys

    in_n = 1260

    print(solution(in_n))
