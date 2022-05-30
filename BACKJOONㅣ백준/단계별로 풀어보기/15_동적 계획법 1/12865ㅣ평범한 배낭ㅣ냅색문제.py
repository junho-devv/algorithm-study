def solution():

    list_item = [[0, 0]]
    for _ in range(in_n):
        list_item.append(list(map(int, sys.stdin.readline().split())))

    knapsack = [[0] * (in_k + 1) for _ in range(in_n + 1)]

    for n in range(1, in_n + 1):
        for k in range(1, in_k + 1):
            weight_n, value_n = list_item[n]

            if k < weight_n:
                knapsack[n][k] = knapsack[n - 1][k]
            else:
                knapsack[n][k] = max(value_n + knapsack[n - 1][k - weight_n], knapsack[n - 1][k])

    answer = knapsack[-1][-1]
    return answer


if __name__ == '__main__':

    import sys

    in_n, in_k = map(int, sys.stdin.readline().split())

    print(solution())

