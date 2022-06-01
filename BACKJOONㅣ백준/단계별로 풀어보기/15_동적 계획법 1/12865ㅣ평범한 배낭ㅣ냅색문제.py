def solution(item, max_weight):

    knapsack = [[0] * (item + 1) for _ in range(max_weight + 1)]

    for n in range(1, max_weight + 1):
        for k in range(1, item + 1):
            weight, value = list_item[n]

            if k < weight:
                knapsack[n][k] = knapsack[n - 1][k]
            else:
                knapsack[n][k] = max(value + knapsack[n - 1][k - weight], knapsack[n - 1][k])

    answer = knapsack[-1][-1]
    return answer


if __name__ == "__main__":

    import sys

    in_n, in_k = map(int, sys.stdin.readline().split())

    list_item = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(in_n)]

    print(solution(in_n, in_k))


